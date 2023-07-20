import addict

import gondi.contracts.abi.auction_loan_liquidator as auction_loan_liquidator
import gondi.rpc as rpc
from gondi.utils import Account
from gondi.contracts.base_contract import BaseContract


class AuctionLoanLiquidator(BaseContract):
    def __init__(self, config: addict.Dict, rpc_client: rpc.RPC, account: Account):
        super().__init__(config, rpc_client, account)
        self._contract = rpc_client.get_contract(
            config.liquidator, auction_loan_liquidator.ABI
        )

    async def add_loan_contract(self, address: str):
        txn = await self._build_wrapper(
            self._contract.functions.addLoanContract, address
        )
        return await self._send_signed_wrapper(txn)

    async def get_valid_loan_contracts(self) -> set[str]:
        return set(await self._contract.functions.getValidLoanContracts().call())
