from enum import Enum
from typing import Any, Generic, TypeVar

from dataclasses import asdict, dataclass

T = TypeVar("T")


class AsKwargsMixin:
    @property
    def as_parameter(self):
        return True

    def as_kwargs(self):
        parsed = self._parsed(asdict(self))
        return (
            {self.lower_first(self.__class__.__name__): parsed}
            if self.as_parameter
            else parsed
        )

    def _parsed(self, value) -> Any | dict[str, Any]:
        if isinstance(value, dict):
            return {
                self.lower_first(self.to_camel_case(k)): self._parsed(v)
                for k, v in value.items()
                if v is not None
            }
        return value

    @staticmethod
    def lower_first(s):
        return s[:1].lower() + s[1:] if s else ""

    @staticmethod
    def to_camel_case(snake_str):
        return "".join(x.capitalize() for x in snake_str.lower().split("_"))


@dataclass(frozen=True)
class NonceInput(AsKwargsMixin):
    wallet_address: str
    blockchain: str


@dataclass(frozen=True)
class SiweInput(AsKwargsMixin):
    message: str
    signature: str


@dataclass(frozen=True)
class UserFilter(AsKwargsMixin):
    user_id: int
    only_or_exclude: bool


@dataclass(frozen=True)
class ListingInput(AsKwargsMixin):
    user_filter: UserFilter | None = None
    collection_ids: list[int] | None = None
    search_term: str | None = None
    with_loans: bool | None = None
    first: int | None = None
    after: str | None = None

    @property
    def as_parameter(self):
        return False


class OfferStatus(Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    EXECUTED = "EXECUTED"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    OUTPERFORMED = "OUTPERFORMED"


class OffersSortField(Enum):
    DURATION = "DURATION"
    TOTAL_INTEREST = "TOTAL_INTEREST"
    PRINCIPAL_AMOUNT = "PRINCIPAL_AMOUNT"
    APR_BPS = "APR_BPS"
    EXPIRATION = "EXPIRATION"
    REPAYMENT = "REPAYMENT"
    CREATED_DATE = "CREATED_DATE"
    STATUS = "STATUS"


class Ordering(Enum):
    ASC = "ASC"
    DESC = "DESC"


class SortInput(Generic[T]):
    field: T
    ordering: str


class OffersSortInput(AsKwargsMixin, SortInput):
    field: OffersSortField


class Interval(AsKwargsMixin):
    min: float | None = None
    max: float | None = None


@dataclass(frozen=True)
class TermsFilter(AsKwargsMixin):
    apr_bps: Interval | None = None
    principal: Interval | None = None
    duration: Interval | None = None


@dataclass(frozen=True)
class OfferInput(AsKwargsMixin):
    lender_address: str | None = None
    borrower_address: str | None = None
    statuses: list[OfferStatus] | None = None
    hidden: bool | None = None
    only_single_nft_offers: bool | None = False
    only_collection_offers: bool | None = False
    sort_by: list[OffersSortInput] | None = None
    nfts: list[int] | None = None
    collections: list[int] | None = None
    first: int | None = 10
    after: str | None = None
    terms: TermsFilter | None = None

    @property
    def as_parameter(self):
        return False
