import addict
from web3.auto import w3

import gondi.contracts.abi.sample_token as sample_token
import gondi.rpc as rpc
from gondi.contracts.base_contract import BaseContract
from gondi.utils import Account


class SampleToken(BaseContract):
    def __init__(self, config: addict.Dict, rpc_client: rpc.RPC, account: Account):
        super().__init__(config, rpc_client, account)
        self._contract = rpc_client.get_contract(config.erc20, sample_token.ABI)

    async def balance_of(self, address: str):
        return await self._contract.functions.balanceOf(address).call()

    async def mint(self, amount: int, address: str | None = None):
        address = w3.to_checksum_address(address) or self._account.public_key
        minted = await self._build_wrapper(
            self._contract.functions.mint, address, amount
        )
        return await self._send_signed_wrapper(minted)

    async def approve(self, amount: int, address: str | None = None):
        address = w3.to_checksum_address(address) or self._account.public_key
        txn = await self._build_wrapper(
            self._contract.functions.approve, address, amount
        )
        return await self._send_signed_wrapper(txn)
