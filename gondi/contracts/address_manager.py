import addict

import gondi.rpc as rpc
import gondi.contracts.abi.address_manager as address_manager
from gondi.utils import Account
from gondi.contracts.base_contract import BaseContract


class AddressManager(BaseContract):
    def __init__(
        self,
        config: "addict.Dict",
        rpc_client: rpc.RPC,
        account: Account,
        contract_address: str,
    ):
        super().__init__(config, rpc_client, account)
        self._contract = rpc_client.get_contract(contract_address, address_manager.ABI)

    async def owner(self) -> str:
        return await self._contract.functions.owner().call()

    async def whitelisted_currencies(self) -> list[str]:
        return await self._contract.functions.getWhitelistedCurrencies().call()

    async def add(self, address: str):
        txn = await self._rpc.build_transaction(self._contract.functions.add, address)
        return await self._send_signed_wrapper(txn)

    async def add_to_whitelist(self, address: str):
        txn = await self._rpc.build_transaction(
            self._contract.functions.addToWhitelist, address
        )
        return await self._send_signed_wrapper(txn)

    async def remove_from_whitelist(self, address: str):
        txn = await self._rpc.build_transaction(
            self._contract.functions.removeFromWhitelist, address
        )
        return await self._send_signed_wrapper(txn)

    async def index_to_address(self, index: int):
        return await self._contract.functions.indexToAddress(index).call()

    async def address_to_index(self, address: str):
        return await self._contract.functions.addressToIndex(address).call()

    async def is_whitelisted(self, address: str) -> bool:
        return await self._contract.functions.isWhitelisted(address).call()
