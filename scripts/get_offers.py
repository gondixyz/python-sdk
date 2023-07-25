from gondi.common_utils import Environment
from gondi.api import inputs
from gondi.api.client import Client


async def test():
    from gondi.api.query_provider import QueryProvider

    client = Client(Environment.MAIN)
    offers_input = inputs.OfferInput(statuses=[inputs.OfferStatus.ACTIVE])
    provider = QueryProvider(client)
    for i in range(300):
        print(await client.query(provider.get_offers(offers_input)))
        print(i)


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()

    loop.run_until_complete(test())
