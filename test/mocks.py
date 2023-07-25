import copy
from typing import Any

from gql import Client
from gql.dsl import DSLQuery

from gondi.common_utils.singleton import Singleton


class MockedAccount:
    def __init__(self):
        self._enabled_hd_wallet = False

    def enable_unaudited_hdwallet_features(self):
        self._enabled_hd_wallet = True

    async def sign_transaction(self, txn, private_key: str):
        return txn


class MockedEth:
    def __init__(self) -> None:
        self._account = MockedAccount()

    @property
    async def chain_id(self):
        return 1

    @property
    def account(self):
        return self._account

    async def get_transaction_count(self, _: str):
        return 1

    async def send_raw_transaction(self, _: str):
        return "test_hash"


class MockedProvider:
    def __init__(self, url: str):
        self._url = url


class MockedWeb3:
    AsyncHTTPProvider = MockedProvider

    def __init__(self, _: MockedProvider):
        self._eth = MockedEth()

    @property
    def eth(self):
        return self._eth

    def to_hex(self, data: bytes) -> str:
        return data.hex()

    def keccak(self, _: str) -> bytes:
        return b"0"


class MockedSession(metaclass=Singleton):
    def __init__(self):
        self._return_values = {
            "generateSignInNonce": 1,
            "signInWithEthereum": "test_bearer",
        }

        self._queries = []

    @property
    def queries(self):
        return self._queries

    @property
    def return_values(self) -> dict[str, Any]:
        return self._return_values

    async def execute(self, query: "DSLQuery") -> dict[str, Any]:
        self._queries.append(query)
        return copy.copy(self._return_values)


class MockedGraphqlClient:
    def __init__(self, schema, transport):
        self._client = Client(schema=schema, transport=transport)
        self._transport = transport

    async def __aenter__(self):
        return MockedSession()

    async def __aexit__(self, *args, **kwargs):
        pass

    @property
    def schema(self):
        return self._client.schema

    @property
    def transport(self):
        return self._transport
