import unittest

from gondi.utils import Environment, load_config


class TestUtils(unittest.IsolatedAsyncioTestCase):
    async def test_load_config(self):
        config = load_config(Environment.LOCAL)
        self.assertEqual(config.rpc_url, "http://127.0.0.1:8545")
        self.assertGreaterEqual(len(config.accounts), 3)
