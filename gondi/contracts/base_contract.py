import addict
from web3.auto import w3

import gondi.rpc as rpc
from gondi.utils import Account, load_config


class BaseContract:
    def __init__(self, config: "addict.Dict", rpc: rpc.RPC, account: Account):
        self._config = load_config(config) if isinstance(config, str) else config
        self._rpc = rpc
        self._account = account
        self._contract = None

    @property
    def contract(self):
        return self._contract

    def with_account(self, account: Account):
        self._account = account
        return self

    async def _build_wrapper(self, *args, **kwargs):
        return await self._rpc.build_transaction(
            self._account.public_key, *args, **kwargs
        )

    async def _send_signed_wrapper(self, txn):
        return await self._rpc.send_txn(
            self._rpc.sign_txn(txn, self._account.private_key),
            self._account.public_key,
        )
