from typing import Any

from dataclasses import asdict, dataclass


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
