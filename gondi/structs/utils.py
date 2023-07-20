import re
from typing import Any

import web3
from Crypto.Hash import keccak
from eth_abi import encode
from eth_abi.packed import encode_packed
from web3 import Web3
from web3.auto import w3


from gondi.utils import Environment, load_config
from gondi.structs.types import ADDRESS, BYTES32, STRING, UINT256, UINT8


DELIM = "\x19\x01"
FIRST_PASS_CAMEL = re.compile("(.)([A-Z][a-z]+)")
SECOND_PASS_CAMEL = re.compile("([a-z0-9])([A-Z])")


def hash(data: bytes) -> bytes:
    k = keccak.new(digest_bits=256)
    k.update(data)
    return k.digest()


def camel_to_snake(name):
    name = FIRST_PASS_CAMEL.sub(r"\1_\2", name)
    return SECOND_PASS_CAMEL.sub(r"\1_\2", name).lower()


def extract_fields(
    result: "web3.datastructures.MutableAttributeDict",
    fields: tuple[str, ...],
    is_private: bool | None = False,
    is_camel_to_snake: bool | None = False,
):
    offset = int(is_private)
    parse = camel_to_snake if is_camel_to_snake else lambda x: x
    return {parse(k[offset:]): v for k, v in result.items() if k[offset:] in fields}


def get_domain_separator(chain_id: int, contract_address: str) -> bytes:
    # keccak256("EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)") # noqa
    eip_keccak = bytes.fromhex(
        "8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f"
    )
    # keccak256("GONDI_MULTI_SOURCE_LOAN")
    contract_keccak = bytes.fromhex(
        "06cee46c5c3730968614d9872085ea89ec832dff1a79917ad243588c9812d9b6"
    )
    # keccak256("1")
    one_keccak = bytes.fromhex(
        "c89efdaa54c0f20c7adf612882df0950f5a951637e0307cdcb4c672f298b8bc6"
    )
    address = bytes.fromhex(contract_address[2:])
    encoded = encode(
        [BYTES32, BYTES32, BYTES32, UINT256, ADDRESS],
        [eip_keccak, contract_keccak, one_keccak, chain_id, address],
    )
    return hash(encoded)


def eip712_hash(obj: Any, chain_id: int, contract_address: str) -> bytes:
    struct_hash = obj.struct_hash()
    domain_separator = get_domain_separator(chain_id, contract_address)
    encoded = encode_packed(
        [STRING, BYTES32, BYTES32],
        [DELIM, domain_separator, struct_hash],
    )
    return hash(encoded)


local_conf = load_config(Environment.LOCAL)


def sign_object(
    obj: Any,
    chain_id: int,
    contract_address: str,
    signer: str,
) -> bytes:
    offer_hash = eip712_hash(obj, chain_id, contract_address)
    signed = w3.eth.account.signHash(offer_hash, private_key=signer)
    return encode_packed(
        [BYTES32, BYTES32, UINT8],
        [Web3.to_bytes(signed.r), Web3.to_bytes(signed.s), Web3.to_int(signed.v)],
    )
