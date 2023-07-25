import unittest
from unittest.mock import patch

from gql.dsl import DSLQuery

from gondi.api.client import Client
from test.mocks import MockedGraphqlClient, MockedSession


GraphqlClientPatch = patch("gql.Client", MockedGraphqlClient)


@GraphqlClientPatch
class TestClient(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self._session = MockedSession()

    async def test_login(self):
        client = Client()
        await client.login()
        self.assertEquals(
            client.bearer, self._session.return_values["signInWithEthereum"]
        )

    async def test_check_bearer(self):
        client = Client()
        await client.check_bearer()
        self.assertEquals(
            client.bearer, self._session.return_values["signInWithEthereum"]
        )

    async def test_query(self):
        client = Client()
        sample_query = self._sample_query(client.lending_schema)
        no_queries = len(self._session.queries)
        await client.query(sample_query)
        self.assertEqual(no_queries + 1, len(self._session.queries))

    async def test_auth_query(self):
        client = Client()
        sample_query = self._sample_query(client.lending_schema)
        await client.auth_query(sample_query)
        self.assertEquals(
            client.bearer, self._session.return_values["signInWithEthereum"]
        )

    def _sample_query(self, schema):
        return DSLQuery(
            schema.Query.listOffers.select(schema.OfferConnection.totalCount)
        )
