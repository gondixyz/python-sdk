import datetime as dt
import os

import gql
from eth_account.messages import encode_defunct
from gql.dsl import dsl_gql, DSLSchema, DSLMutation, DSLQuery
from gql.transport.aiohttp import AIOHTTPTransport
from siwe import SiweMessage
from web3.auto import w3

import gondi.api.inputs as inputs
from gondi.common_utils import load_config, Environment
from gondi.common_utils.singleton import Singleton

DOMAIN = "localhost"
URI = f"http://{DOMAIN}"
STATEMENT = "Sign in with Ethereum to the app."


def requires_login(fn):
    async def check_login(self, *args, **kwargs):
        await self.check_bearer()
        return await fn(self, *args, **kwargs)

    return check_login


class Client(metaclass=Singleton):
    def __init__(self, env: Environment | None = Environment.LOCAL):
        config = load_config(env)
        self._client = gql.Client(
            schema=self._get_schema("base_schema"),
            transport=AIOHTTPTransport(url=config.api_url),
        )
        self._lending_client = gql.Client(
            schema=self._get_schema("lending_schema"),
            transport=AIOHTTPTransport(url=config.lending_api_url),
        )
        self._ds = DSLSchema(self._client.schema)
        self._lending_ds = DSLSchema(self._lending_client.schema)
        self._account = config.accounts[0]
        self._blockchain = config.blockchain
        self._version = config.client_version
        self._chain_id = config.chain_id
        self._bearer = None

    @property
    def schema(self) -> "DSLSchema":
        return self._ds

    @property
    def lending_schema(self) -> "DSLSchema":
        return self._lending_ds

    async def login(self):
        nonce = await self._get_nonce()
        message = self._get_siwe_message(nonce)
        encoded = encode_defunct(text=message)
        signed = w3.eth.account.sign_message(encoded, self._account.private_key)
        signature = signed.signature.hex()
        siwe_input = inputs.SiweInput(message, signature)
        query = DSLMutation(
            self._ds.Mutation.signInWithEthereum.args(**siwe_input.as_kwargs())
        )
        async with self._client as session:
            result = await session.execute(dsl_gql(query))
        self._bearer = result["signInWithEthereum"]
        self._update_headers(self._bearer)

    async def check_bearer(self):
        # TODO: Check whether token is expired
        if self._bearer is None:
            await self.login()

    async def query(self, query: "DSLQuery") -> dict:
        async with self._lending_client as session:
            return await session.execute(dsl_gql(query))

    @requires_login
    async def auth_query(self, query: "DSLQuery") -> dict:
        async with self._lending_client as session:
            return await session.execute(dsl_gql(query))

    def _update_headers(self, bearer: str):
        self._client.transport.headers = {"Authorization": f"Bearer {bearer}"}
        self._lending_client.transport.headers = {"Authorization": f"Bearer {bearer}"}

    async def _get_nonce(self) -> str:
        nonce_input = inputs.NonceInput(self._account.public_key, self._blockchain)
        query = DSLMutation(
            self._ds.Mutation.generateSignInNonce.args(**nonce_input.as_kwargs())
        )
        async with self._client as session:
            return (await session.execute(dsl_gql(query)))["generateSignInNonce"]

    def _get_siwe_message(self, nonce: str) -> SiweMessage:
        return SiweMessage.construct(
            domain=DOMAIN,
            statement=STATEMENT,
            address=self._account.public_key,
            uri=URI,
            version=self._version,
            chain_id=self._chain_id,
            issued_at=dt.datetime.now().astimezone().isoformat(),
            nonce=nonce,
        ).prepare_message()

    @staticmethod
    def _get_schema(schema: str) -> str:
        base_dir = f"{os.path.dirname(os.path.realpath(__file__))}/../resources"
        filename = f"{base_dir}/{schema}.graphql"
        with open(filename) as f:
            return f.read()


async def test():
    from gondi.api.query_provider import QueryProvider

    client = Client(Environment.MAIN)
    offers_input = inputs.OfferInput(only_single_nft_offers=True)
    provider = QueryProvider(client)
    print(await client.query(provider.get_offers(offers_input)))


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()

    loop.run_until_complete(test())
