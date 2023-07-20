import time
from typing import Any, NamedTuple

import web3
from eth_abi import encode
from eth_abi.packed import encode_packed

from gondi.utils import Environment, load_config
from gondi.structs.types import ADDRESS, BYTES32, UINT256
from gondi.structs.utils import extract_fields, hash

local_conf = load_config(Environment.LOCAL)


class OfferValidator(NamedTuple):
    validator: str
    arguments: bytes

    def as_array(self) -> list[Any]:
        return [self.validator, self.arguments]

    def struct_signature(self) -> bytes:
        return bytes.fromhex(
            "4def3e04bd42194484d5f8a5b268ec0df03b9d9d0402606fe3100023c5d79ac4"
        )

    def struct_hash(self) -> bytes:
        encoded = encode(
            [BYTES32, ADDRESS, "bytes32"],
            [self.struct_signature(), self.validator, hash(self.arguments)],
        )
        return hash(encoded)


class BaseLoanOffer(NamedTuple):
    offerId: int
    lender: str
    fee: int
    borrower: str
    capacity: int
    signer: str
    requiresLiquidation: bool
    nftCollateralAddress: str
    nftCollateralTokenId: int
    principalAddress: str
    principalAmount: int
    aprBps: int
    expirationTime: int
    duration: int
    validators: list[OfferValidator]
    contractAddress: str | None = None

    _INTERNAL_FIELDS = ("contractAddress",)

    @classmethod
    def from_loan_emit_input(
        cls,
        result: "web3.datastructures.MutableAttributeDict",
        contractAddress: str | None = None,
    ) -> "BaseLoanOffer":
        offer = result._loanOffer
        offer_raw = extract_fields(offer, cls._fields)
        offer_raw["validators"] = [
            OfferValidator(**extract_fields(validator, OfferValidator._fields))
            for validator in offer["validators"]
        ]
        return BaseLoanOffer(contractAddress=contractAddress, **offer_raw)

    @classmethod
    def struct_signature(cls) -> bytes:
        # keccak256("LoanOffer(uint256 offerId,address lender,uint256 fee,address borrower,uint256 capacity,address signer,bool requiresLiquidation,address nftCollateralAddress,uint256 nftCollateralTokenId,address principalAddress,uint256 principalAmount,uint256 aprBps,uint256 expirationTime,uint256 duration,OfferValidator[] validators)OfferValidator(address validator,bytes arguments)") # noqa
        return bytes.fromhex(
            "06e76f1058ba8fa0e93e1abebc67277f42f2293296709705f282301940665901"
        )

    def abi_compatible(self) -> dict[str, Any]:
        base = self._asdict()
        for field in self._INTERNAL_FIELDS:
            del base[field]
        return base

    def struct_hash(self) -> bytes:
        encoded_types = [
            BYTES32,
            UINT256,
            ADDRESS,
            UINT256,
            ADDRESS,
            UINT256,
            ADDRESS,
            UINT256,
            ADDRESS,
            UINT256,
            ADDRESS,
            UINT256,
            UINT256,
            UINT256,
            UINT256,
            BYTES32,
        ]

        encoded = encode(
            encoded_types,
            [
                self.struct_signature(),
                int(self.offerId),
                self.lender,
                self.fee,
                self.borrower,
                self.capacity,
                self.signer,
                int(self.requiresLiquidation),
                self.nftCollateralAddress,
                int(self.nftCollateralTokenId),
                self.principalAddress,
                int(self.principalAmount),
                int(self.aprBps),
                int(self.expirationTime),
                int(self.duration),
                hash(b"".join(v.struct_hash() for v in self.validators)),
            ],
        )
        return hash(encoded)

    @staticmethod
    def get_sample_offer(**kwargs) -> "BaseLoanOffer":
        defaults = BaseLoanOffer._get_defaults()
        defaults["validators"] = []
        for k, v in kwargs.items():
            defaults[k] = v
        return BaseLoanOffer(**defaults)

    @staticmethod
    def _get_defaults() -> dict[str, Any]:
        return {
            "contractAddress": local_conf.multi_source_loan,
            "offerId": 1,
            "lender": local_conf.accounts[0].public_key,
            "fee": 0,
            "signer": local_conf.accounts[0].public_key,
            "borrower": local_conf.accounts[2].public_key,
            "capacity": 0,
            "requiresLiquidation": True,
            "nftCollateralAddress": local_conf.erc721,
            "nftCollateralTokenId": 1,
            "principalAddress": local_conf.erc20,
            "principalAmount": int(1e18),
            "aprBps": 1000,
            "expirationTime": int(time.time() + 120000000),
            "duration": 100000,
        }


class Source(NamedTuple):
    loanId: int
    lender: str
    principalAmount: int
    accruedInterest: int
    startTime: int
    aprBps: int

    @classmethod
    def struct_hash(cls) -> bytes:
        # keccak256("Source(uint256 loanId,address lender,uint256 principalAmount,uint256 accruedInterest,uint256 startTime,uint256 aprBps)") # noqa
        return bytes.fromhex(
            "8ca047c2f10359bf4a27bd2c623674be3801153b6b2646ba08593dc96ad7bb44"
        )

    def abi_compatible(self) -> dict[str, Any]:
        return self._asdict()


class MultiSourceLoan(NamedTuple):
    contractAddress: str
    loanId: int
    offerId: int
    borrower: str
    nftCollateralTokenId: int
    nftCollateralAddress: str
    principalAddress: str
    principalAmount: int
    startTime: int
    duration: int
    source: list[Source]
    fee: int

    _INTERNAL_FIELDS = ("contractAddress", "loanId", "offerId", "fee")

    @classmethod
    def struct_signature(cls) -> bytes:
        # keccak256("Loan(address borrower,uint256 nftCollateralTokenId,address nftCollateralAddress,address principalAddress,uint256 principalAmount,uint256 startTime,uint256 duration,Source[] source)Source(uint256 loanId,address lender,uint256 principalAmount,uint256 accruedInterest,uint256 startTime,uint256 aprBps)") # noqa
        return bytes.fromhex(
            "35f73c5cb07b3fa605378d4f576769166fed212ec3813ac1f1d73ef1c537eb0e"
        )

    @classmethod
    def from_emit(cls, result: "web3.datastructures.MutableAttributeDict"):
        loan_dict = result.args.loan
        loan_raw = extract_fields(loan_dict, cls._fields)
        source_raw = extract_fields(loan_dict["source"][0], Source._fields)
        loan_raw["source"] = [Source(**source_raw)]
        loan_raw["loanId"] = result.args.loanId
        loan_raw["offerId"] = result.args.offerId
        loan_raw["fee"] = result.args.fee
        source_raw["accruedInterest"] = 0
        return cls(contractAddress=result.address.lower(), **loan_raw)

    @classmethod
    def from_refinance(cls, result: "web3.datastructures.MutableAttributeDict"):
        loan_dict = result.args["loan"]
        loan_raw = extract_fields(loan_dict, cls._fields)
        loan_raw["source"] = [
            Source(**extract_fields(source, Source._fields))
            for source in loan_dict["source"]
        ]
        return cls(
            contractAddress=result.address.lower(),
            loanId=result.args.newLoanId,
            fee=result.args.fee,
            offerId=result.args.renegotiationId,
            **loan_raw
        )

    def abi_compatible(self) -> dict[str, Any]:
        base = self._asdict()
        for field in self._INTERNAL_FIELDS:
            del base[field]
        base["source"] = [source.abi_compatible() for source in base["source"]]
        return base

    def struct_hash(self) -> bytes:
        encoded_types = [
            BYTES32,
            ADDRESS,
            UINT256,
            ADDRESS,
            ADDRESS,
            UINT256,
            UINT256,
            UINT256,
            BYTES32,
        ]
        sources_hash = self._encoded_sources()
        encoded = encode(
            encoded_types,
            [
                self.struct_signature(),
                self.borrower,
                int(self.nftCollateralTokenId),
                self.nftCollateralAddress,
                self.principalAddress,
                int(self.principalAmount),
                int(self.startTime),
                int(self.duration),
                sources_hash,
            ],
        )
        return hash(encoded)

    def _encoded_sources(self) -> bytes:
        hashes = [self._hash_source(source) for source in self.source]
        encoded = encode_packed([BYTES32] * len(hashes), hashes)
        return hash(encoded)

    @staticmethod
    def _hash_source(source):
        encoded_types = [
            BYTES32,
            ADDRESS,
            UINT256,
            UINT256,
            UINT256,
            UINT256,
        ]
        encoded = encode(
            encoded_types,
            [
                source.struct_hash(),
                source.lender,
                source.principalAmount,
                source.accruedInterest,
                source.startTime,
                source.aprBps,
            ],
        )
        return hash(encoded)


class RenegotiationOffer(NamedTuple):
    renegotiationId: int
    loanId: int
    lender: str
    fee: int
    signer: int
    targetPrincipal: list[int]
    principalAmount: int
    aprBps: int
    expirationTime: int
    duration: int
    strictImprovement: bool

    @classmethod
    def from_renegotiation_input(
        cls, result: "web3.datastructures.MutableAttributeDict"
    ):
        return RenegotiationOffer(
            **extract_fields(result["_renegotiationOffer"], cls._fields)
        )

    def abi_compatible(self) -> dict[str, Any]:
        return self._asdict()

    def struct_signature(self) -> bytes:
        return bytes.fromhex(
            "03ac2651e1cbec1c7c1a8a4a4fe765ccbaa390095e5f4c3212468e5412035857"
        )

    def struct_hash(self) -> bytes:
        encoded_types = [
            BYTES32,
            UINT256,
            UINT256,
            ADDRESS,
            UINT256,
            ADDRESS,
            BYTES32,
            UINT256,
            UINT256,
            UINT256,
            UINT256,
            UINT256,
        ]
        encoded = encode(
            encoded_types,
            [
                self.struct_signature(),
                self.renegotiationId,
                self.loanId,
                self.lender,
                self.fee,
                self.signer,
                hash(b"".join(encode([UINT256], [v]) for v in self.targetPrincipal)),
                self.principalAmount,
                self.aprBps,
                self.expirationTime,
                self.duration,
                int(self.strictImprovement),
            ],
        )
        return hash(encoded)

    @staticmethod
    def get_sample_partial_offer(
        loan: "MultiSourceLoan", **kwargs
    ) -> "RenegotiationOffer":
        amount = int(loan.source[0].principalAmount / 2)
        lender = local_conf.accounts[1].public_key
        target_principal = [loan.source[0].principalAmount - amount]
        defaults = RenegotiationOffer._get_defaults(
            loan, amount, lender, target_principal, 0
        )
        for k, v in kwargs.items():
            defaults[k] = v
        return RenegotiationOffer(**defaults)

    @staticmethod
    def get_sample_full_offer(
        loan: "MultiSourceLoan", **kwargs
    ) -> "RenegotiationOffer":
        amount = loan.principalAmount
        lender = local_conf.accounts[2].public_key
        target_principal = [0] * len(loan.source)
        defaults = RenegotiationOffer._get_defaults(
            loan, amount, lender, target_principal, loan.duration
        )

        for k, v in kwargs.items():
            defaults[k] = v
        return RenegotiationOffer(**defaults)

    @staticmethod
    def _get_defaults(
        loan: "MultiSourceLoan",
        amount: int,
        lender: str,
        target_principal: list[int],
        duration: int,
    ) -> dict[str, Any]:
        return {
            "renegotiationId": 1,
            "loanId": loan.loanId,
            "lender": lender,
            "fee": 0,
            "signer": lender,
            "targetPrincipal": target_principal,
            "principalAmount": amount,
            "aprBps": int(loan.source[0].aprBps / 2),
            "expirationTime": int(time.time() + 120000000),
            "duration": duration,
            "strictImprovement": True,
        }
