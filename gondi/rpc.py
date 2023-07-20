from collections import defaultdict
from typing import Callable

import tenacity
from web3 import AsyncWeb3
from web3.auto import w3

MAX_WAIT = 5
WAIT = 0.5
MAX_FEE_PER_GAS = w3.to_wei("25", "gwei")


def requires_start(fn):
    async def call_start(self, *args, **kwargs):
        await self.start()
        return await fn(self, *args, **kwargs)

    return call_start


class RPC:
    def __init__(self, rpc_url: str):
        self._web3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(rpc_url))
        self._started = False
        self._nonce = {}

    @property
    def chain_id(self):
        return self._chain_id

    async def start(self):
        self._chain_id = await self._web3.eth.chain_id
        self._web3.eth.account.enable_unaudited_hdwallet_features()
        self._nonce = defaultdict(lambda: 0)
        self._started = True

    @requires_start
    async def get_nonce(self, public_key: str):
        return await self._web3.eth.get_transaction_count(public_key)

    @requires_start
    async def build_transaction(self, public_key: str, fn: Callable, *args):
        public_key = w3.to_checksum_address(public_key)
        nonce = max(self._nonce[public_key], await self.get_nonce(public_key))
        return await fn(*args).build_transaction(
            {
                "value": 0,
                "gas": 5000000,
                "chainId": self.chain_id,
                "maxFeePerGas": MAX_FEE_PER_GAS,
                "nonce": nonce,
            }
        )

    def sign_txn(self, txn, private_key):
        return self._web3.eth.account.sign_transaction(txn, private_key=private_key)

    @requires_start
    async def send_txn(self, signed_txn, public_key):
        self._nonce[public_key] += 1
        await self._web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return self._web3.to_hex(self._web3.keccak(signed_txn.rawTransaction))

    @requires_start
    async def get_txn_receipt(self, txn):
        receipt = None
        async for attempt in tenacity.AsyncRetrying(
            wait=tenacity.wait.wait_exponential(WAIT),
            stop=tenacity.stop.stop_after_attempt(MAX_WAIT),
        ):
            with attempt:
                receipt = await self._web3.eth.get_transaction_receipt(txn)
        return receipt

    def get_contract(self, address: str, abi: list[dict]):
        return self._web3.eth.contract(address=w3.to_checksum_address(address), abi=abi)
