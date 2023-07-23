import addict
from web3.auto import w3

import gondi.contracts.abi.sample_collection as sample_collection
import gondi.common_utils.rpc as rpc
from gondi.contracts.base_contract import BaseContract
from gondi.common_utils.utils import Account


class SampleCollection(BaseContract):
    def __init__(
        self,
        config: addict.Dict,
        rpc_client: rpc.RPC,
        account: Account,
        contract_address: str | None = None,
    ):
        super().__init__(config, rpc_client, account)
        self._contract = rpc_client.get_contract(
            contract_address if contract_address else config.erc721,
            sample_collection.ABI,
        )

    async def mint_next(self, address: str | None = None):
        address = w3.to_checksum_address(address) or self._account.public_key
        minted = await self._build_wrapper(self._contract.functions.mintNext, address)
        return await self._send_signed_wrapper(minted)

    async def mint(self, nft_id: int, address: str | None = None):
        address = w3.to_checksum_address(address) or self._account.public_key
        minted = await self._build_wrapper(
            self._contract.functions.mint, address, nft_id
        )
        return await self._send_signed_wrapper(minted)

    async def approve(self, nft_id: int, address: str | None = None):
        address = w3.to_checksum_address(address) or self._account.public_key
        minted = await self._build_wrapper(
            self._contract.functions.approve, address, nft_id
        )
        return await self._send_signed_wrapper(minted)

    async def owner_of(self, nft_id: int):
        return await self._contract.functions.ownerOf(nft_id).call()
