import logging

import gondi.contracts as contracts
from web3.datastructures import MutableAttributeDict

from gondi.rpc import RPC
from gondi.structs.loan import BaseLoanOffer, MultiSourceLoan, RenegotiationOffer
from gondi.structs.utils import sign_object
from gondi.utils import (
    Account,
    Environment,
    load_config,
)

logging.getLogger().setLevel(logging.INFO)

TOKENS = int(1e20)


async def mint_tokens(
    contract: contracts.SampleToken, loan_contract: str, account: Account
):
    await contract.with_account(account).mint(TOKENS, account.public_key)
    await contract.with_account(account).approve(TOKENS, loan_contract)
    logging.info("Minted lender tokens")


async def mint_next(
    rpc: RPC, contract: contracts.SampleCollection, loan_contract: str, account: Account
) -> int:
    txn = await contract.mint_next(account.public_key)
    receipt = await rpc.get_txn_receipt(txn)
    log = contract.contract.events.Transfer().process_log(receipt.logs[-1])
    nft_id = log.args.id
    await contract.approve(nft_id, loan_contract)
    logging.info("Minted NFT: %s", nft_id)
    return nft_id


async def emit_loan(
    rpc: RPC,
    contract: contracts.MultiSourceLoan,
    offer: BaseLoanOffer,
    signature: bytes,
) -> MultiSourceLoan:
    txn = await contract.emit_loan(offer, offer.nftCollateralTokenId, signature)
    receipt = await rpc.get_txn_receipt(txn)
    raw_loan = MutableAttributeDict(
        contract.contract.events.LoanEmitted().process_log(receipt.logs[-1])
    )
    logging.info("Loan Emitted")
    return MultiSourceLoan.from_emit(raw_loan)


async def refinance_partial_loan(
    rpc: RPC,
    contract: contracts.MultiSourceLoan,
    refinancer: Account,
    refinance_partial_offer: RenegotiationOffer,
    loan: MultiSourceLoan,
) -> MultiSourceLoan:
    txn = await contract.with_account(refinancer).refinance_partial(
        refinance_partial_offer, loan
    )
    receipt = await rpc.get_txn_receipt(txn)
    raw_renegotiated = contract.contract.events.LoanRefinanced().process_log(
        receipt.logs[-1]
    )
    logging.info("Partial Refinance")
    return loan.from_refinance(raw_renegotiated)


async def refinance_full_loan(
    rpc: RPC,
    contract: contracts.MultiSourceLoan,
    refinancer: Account,
    refinance_full_offer: RenegotiationOffer,
    signature: bytes,
    loan: MultiSourceLoan,
) -> MultiSourceLoan:
    txn = await contract.with_account(refinancer).refinance_full(
        refinance_full_offer, loan, signature
    )
    receipt = await rpc.get_txn_receipt(txn)
    raw_renegotiated = contract.contract.events.LoanRefinanced().process_log(
        receipt.logs[-1]
    )
    logging.info("Full Refinance")
    return loan.from_refinance(raw_renegotiated)


async def repay_loan(
    rpc: RPC,
    contract: contracts.MultiSourceLoan,
    borrower: Account,
    loan: MultiSourceLoan,
):
    txn = await contract.with_account(borrower).repay_loan(
        borrower.public_key, loan.source[0].loanId, loan, False
    )
    receipt = await rpc.get_txn_receipt(txn)
    repayment = contract.contract.events.LoanRepaid().process_log(receipt.logs[-2])
    logging.info("Repayment event: %s", repayment)


async def run():
    config = load_config(Environment.LOCAL)
    lender, refinancer, borrower = config.accounts
    rpc = RPC(config.rpc_url)

    c_sample_token = contracts.SampleToken(config, rpc, lender)

    # Mint lender tokens
    await mint_tokens(c_sample_token, config.multi_source_loan, lender)

    # Mint borrower tokens
    await mint_tokens(c_sample_token, config.multi_source_loan, borrower)

    # Mint Refinancer tokens
    await mint_tokens(c_sample_token, config.multi_source_loan, refinancer)

    # Mint NFT
    c_sample_collection = contracts.SampleCollection(config, rpc, borrower)
    nft_id = await mint_next(
        rpc, c_sample_collection, config.multi_source_loan, borrower
    )

    # Sample loan
    offer = BaseLoanOffer.get_sample_offer(
        borrower=borrower.public_key, nftCollateralTokenId=nft_id, capacity=int(1e32)
    )
    signature = sign_object(
        offer, rpc.chain_id, config.multi_source_loan, lender.private_key
    )
    c_ms_loan = contracts.MultiSourceLoan(config, rpc, borrower)
    loan = await emit_loan(rpc, c_ms_loan, offer, signature)

    # Partial refinance
    refinance_partial_offer = RenegotiationOffer.get_sample_partial_offer(
        loan, lender=refinancer.public_key, signer=refinancer.public_key
    )
    loan = await refinance_partial_loan(
        rpc, c_ms_loan, refinancer, refinance_partial_offer, loan
    )

    # Refinance full
    refinance_full_offer = RenegotiationOffer.get_sample_full_offer(
        loan, lender=lender.public_key, signer=lender.public_key
    )
    loan = await refinance_full_loan(
        rpc, c_ms_loan, lender, refinance_full_offer, signature, loan
    )

    # Repayment
    await repay_loan(rpc, c_ms_loan, borrower, loan)


if __name__ == "__main__":
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(description="Basic Ecosystem Setup")

    loop = asyncio.new_event_loop()
    loop.run_until_complete(run())
