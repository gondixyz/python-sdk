import unittest
from unittest.mock import patch

from gondi.rpc import RPC
from test.mocks import MockedWeb3


Web3Patch = patch("web3.AsyncWeb3", MockedWeb3)


@Web3Patch
class TestRPC(unittest.IsolatedAsyncioTestCase):
    async def test_start(self):
        rpc = RPC("test_url")
        await rpc.start()
