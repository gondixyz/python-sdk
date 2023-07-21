import addict

import gondi.rpc as rpc
import gondi.contracts.abi.multi_source_loan as loan
import gondi.structs.loan as structs
from gondi.utils import Account
from gondi.contracts.base_contract import BaseContract


class MultiSourceLoan(BaseContract):
    def __init__(self, config: addict.Dict, rpc_client: rpc.RPC, account: Account):
        super().__init__(config, rpc_client, account)
        self._contract = rpc_client.get_contract(config.multi_source_loan, loan.ABI)

    async def emit_loan(
        self,
        offer: structs.BaseLoanOffer,
        token_id: int,
        signature: bytes,
        with_callback: bool | None = False,
    ):
        txn = await self._build_wrapper(
            self._contract.functions.emitLoan,
            offer.abi_compatible(),
            token_id,
            signature,
            with_callback,
        )
        return await self._send_signed_wrapper(txn)

    async def refinance_full(
        self,
        offer: structs.RenegotiationOffer,
        existing_loan: structs.MultiSourceLoan,
        signature: bytes,
    ):
        txn = await self._build_wrapper(
            self._contract.functions.refinanceFull,
            offer.abi_compatible(),
            existing_loan.abi_compatible(),
            signature,
        )
        return await self._send_signed_wrapper(txn)

    async def refinance_partial(
        self, offer: structs.RenegotiationOffer, existing_loan: structs.MultiSourceLoan
    ):
        txn = await self._build_wrapper(
            self._contract.functions.refinancePartial,
            offer.abi_compatible(),
            existing_loan.abi_compatible(),
        )
        return await self._send_signed_wrapper(txn)

    async def repay_loan(
        self,
        collateral_recipient: str,
        loan_id: int,
        existing_loan: structs.MultiSourceLoan,
        with_callback: bool | None = False,
    ):
        txn = await self._build_wrapper(
            self._contract.functions.repayLoan,
            collateral_recipient,
            loan_id,
            existing_loan.abi_compatible(),
            with_callback,
        )
        return await self._send_signed_wrapper(txn)

    async def liquidate_loan(
        self, loan_id: int, existing_loan: structs.MultiSourceLoan
    ):
        txn = await self._build_wrapper(
            self._contract.functions.liquidateLoan,
            loan_id,
            existing_loan.abi_compatible(),
        )
        return await self._send_signed_wrapper(txn)

    async def cancel_offer(self, lender: str, offer_id: int):
        txn = await self._build_wrapper(
            self._contract.functions.cancelOffer,
            lender,
            offer_id,
        )
        return await self._send_signed_wrapper(txn)

    async def cancel_all_offers(self, lender: str, min_offer_id: int):
        txn = await self._build_wrapper(
            self._contract.functions.cancelAllOffers,
            lender,
            min_offer_id,
        )
        return await self._send_signed_wrapper(txn)

    async def cancel_renegotiation_offer(self, lender: str, renegotiation_id: int):
        txn = await self._build_wrapper(
            self._contract.functions.cancelRenegotiationOffer,
            lender,
            renegotiation_id,
        )
        return await self._send_signed_wrapper(txn)

    async def cancel_all_renegotiation_offers(
        self, lender: str, min_renegotiation_id: int
    ):
        txn = await self._build_wrapper(
            self._contract.functions.cancelAllRenegotiationOffers,
            lender,
            min_renegotiation_id,
        )
        return await self._send_signed_wrapper(txn)

    async def owner(self):
        return await self._contract.functions.owner().call()

    async def get_total_loans_issued(self):
        return await self._contract.functions.getTotalLoansIssued().call()

    async def get_loan_hash(self, loan_id: int):
        return (await self._contract.functions.getLoanHash(loan_id).call()).hex()

    async def is_offer_valid(self, vault: str, offer_id: int):
        return not await self._contract.functions.isOfferCancelled(
            vault, offer_id
        ).call()
