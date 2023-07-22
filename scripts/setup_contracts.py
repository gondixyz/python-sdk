import asyncio
import logging

import addict

import gondi.contracts as contracts
from gondi.common_utils.rpc import RPC
from gondi.common_utils.utils import Account, Environment, load_config

logging.getLogger().setLevel(logging.INFO)


async def whitelist_currency(config: addict.Dict, rpc: RPC, account: Account):
    erc20 = config.erc20
    address_manager_currencies = contracts.AddressManager(
        config, rpc, account, config.currency_manager
    )
    if not await address_manager_currencies.is_whitelisted(erc20):
        await address_manager_currencies.add(erc20)
        logging.info(f"Added {erc20} to currency manager")


async def whitelist_collections(
    config: addict.Dict,
    rpc: RPC,
    account: Account,
    collections: list[str] | None = None,
):
    erc721 = config.erc721

    address_manager_currencies = contracts.AddressManager(
        config, rpc, account, config.collection_manager
    )
    collections = collections or [erc721]
    for collection in collections:
        if not await address_manager_currencies.is_whitelisted(collection):
            await address_manager_currencies.add(collection)
            logging.info(f"Added {collection} to collection manager")


async def add_loan_to_liquidator(config: addict.Dict, rpc: RPC, account: Account):
    auction_loan_liquidator = contracts.AuctionLoanLiquidator(config, rpc, account)
    valid_contracts = await auction_loan_liquidator.get_valid_loan_contracts()
    msl_address = config.multi_source_loan
    if msl_address not in valid_contracts:
        await auction_loan_liquidator.add_loan_contract(msl_address)
        logging.info(f"Added {msl_address} to liquidator")


async def setup(env: str):
    config = load_config(env)
    rpc = RPC(config.rpc_url)

    await whitelist_currency(config, rpc, config.accounts[0])
    await whitelist_collections(
        config,
        rpc,
        config.accounts[0],
    )
    await add_loan_to_liquidator(config, rpc, config.accounts[0])


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(setup(Environment.LOCAL))
