from gql.dsl import DSLInlineFragment, DSLQuery, DSLSelectable

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
        return DSLQuery(
            lending_schema.Query.listListings.args(**listings_input.as_kwargs()).select(
                connection.totalCount,
                connection.edges.select(
                    edge.node.select(
                        node.id,
                        node.createdDate,
                        node.user.select(lending_schema.User.id),
                        self._with_nft_base_fields(node.nft),
                    )
                ),
            )
        )

    def get_offers(self, offer_input: "OfferInput") -> "DSLQuery":
        lending_schema = self._client.lending_schema
        connection = lending_schema.OfferConnection
        edge = lending_schema.OfferEdge
        node = lending_schema.Offer
        single_nft_offer = DSLInlineFragment()
        single_nft_offer.on(lending_schema.SingleNFTOffer).select(
            self._with_nft_base_fields(lending_schema.SingleNFTOffer.nft)
        )
        collection_offer = DSLInlineFragment()
        collection_offer.on(lending_schema.CollectionOffer).select(
            self._with_contract_address(lending_schema.CollectionOffer.collection)
        )
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
                        single_nft_offer,
                        collection_offer,
                    )
                ),
            )
        )

    def _with_nft_base_fields(self, query: "DSLQuery") -> "DSLSelectable":
        lending_schema = self._client.lending_schema
        nft = lending_schema.NFT
        return query.select(nft.tokenId, self._with_contract_address(nft.collection))

    def _with_contract_address(self, query: "DSLQuery") -> "DSLSelectable":
        lending_schema = self._client.lending_schema
        return query.select(
            lending_schema.Collection.contract_data.select(
                lending_schema.ContractData.contractAddress
            )
        )
