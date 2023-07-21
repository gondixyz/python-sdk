import unittest
from typing import Any, Self
from unittest.mock import patch

from gondi.rpc import RPC, DEFAULT_GAS
from test.mocks import MockedWeb3


Web3Patch = patch("web3.AsyncWeb3", MockedWeb3)


class MockCallableFn:
    def __init__(self, *args, **kwargs):
        self._values = {}

    @property
    def values(self):
        return self._values

    async def build_transaction(self, values: dict[str, Any]) -> Self:
        self._values = values
        return self

    @property
    def rawTransaction(self) -> dict:
        return b"0"


@Web3Patch
class TestRPC(unittest.IsolatedAsyncioTestCase):
    async def test_start(self):
        rpc = RPC("test_url")
        await rpc.start()

        self.assertEqual(rpc.chain_id, 1)

    async def test_get_nonce(self):
        rpc = RPC("test_url")
        await rpc.start()
        nonce = await rpc.get_nonce("")

        self.assertEqual(nonce, 1)

    async def test_build_transaction(self):
        rpc = RPC("test_url")
        await rpc.start()
        txn = await rpc.build_transaction(f"0x{0:040}", MockCallableFn)

        self.assertEqual(txn.values["value"], 0)
        self.assertEqual(txn.values["gas"], DEFAULT_GAS)
        self.assertEqual(txn.values["chainId"], rpc.chain_id)

    async def test_sign_txn(self):
        rpc = RPC("test_url")
        await rpc.start()
        txn = await rpc.build_transaction(f"0x{0:040}", MockCallableFn)

        signed_txn = await rpc.sign_txn(txn, "test_private_key")

        self.assertEqual(txn, signed_txn)

    async def test_send_txn(self):
        rpc = RPC("test_url")
        await rpc.start()
        txn = await rpc.build_transaction(f"0x{0:040}", MockCallableFn)

        signed_txn = await rpc.sign_txn(txn, "test_private_key")

        sent = await rpc.send_txn(signed_txn, public_key="test_public_key")

        self.assertEqual(sent, b"0".hex())
