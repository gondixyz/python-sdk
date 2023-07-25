from gql.dsl import DSLQuery

from gondi.api.inputs import ListingInput, OfferInput
from gondi.api.client import Client
from gondi.common_utils.singleton import Singleton


class QueryProvider(metaclass=Singleton):
    def __init__(self, client: "Client"):
        self._client = client

    def get_listings(self, listings_input: "ListingInput") -> "DSLQuery":
        lending_schema = self._client.lending_schema
        connection = lending_schema.ListingConnection
        edge = lending_schema.ListingEdge
        node = lending_schema.Listing
        nft = lending_schema.NFT
        return DSLQuery(
            lending_schema.Query.listListings.args(**listings_input.as_kwargs()).select(
                connection.totalCount,
                connection.edges.select(
                    edge.node.select(
                        node.id,
                        node.createdDate,
                        node.user.select(lending_schema.User.id),
                        node.nft.select(
                            nft.id,
                            nft.tokenId,
                            nft.collection.select(
                                lending_schema.Collection.contract_data.select(
                                    lending_schema.ContractData.contractAddress
                                )
                            ),
                        ),
                    )
                ),
            )
        )

    def get_offers(self, offer_input: "OfferInput") -> "DSLQuery":
        lending_schema = self._client.lending_schema
        connection = lending_schema.OfferConnection
        edge = lending_schema.OfferEdge
        node = lending_schema.Offer
        nft = lending_schema.NFT
        return DSLQuery(
            lending_schema.Query.listOffers.args(**offer_input.as_kwargs()).select(
                connection.totalCount,
                connection.edges.select(
                    edge.node.select(
                        node.id,
                        node.offerId,
                        node.createdDate,
                        node.borrowerAddress,
                        node.lenderAddress,
                        node.signerAddress,
                        node.capacity,
                        node.expirationTime,
                        node.duration,
                        node.status,
                        node.aprBps,
                        node.fee,
                        node.offerHash,
                        node.signature,
                        node.nft.select(
                            nft.id,
                            nft.tokenId,
                            nft.collection.select(
                                lending_schema.Collection.contract_data.select(
                                    lending_schema.ContractData.contractAddress
                                )
                            ),
                        ),
                    )
                ),
            )
        )
