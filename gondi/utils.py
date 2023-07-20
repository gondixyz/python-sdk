import os
from enum import Enum
from typing import NamedTuple

import yaml
from addict import Dict
from web3.auto import w3


class Environment(Enum):
    LOCAL = "local"
    GOERLI = "goerli"
    MAIN = "main"


class Account(NamedTuple):
    public_key: str
    private_key: str


def load_config(env: Environment) -> Dict:
    base_dir = f"{os.path.dirname(os.path.realpath(__file__)) }/resources"
    filename = f"{base_dir}/config.{env.value}"
    with open(filename) as f:
        raw = Dict({k.lower(): v for k, v in yaml.load(f, yaml.Loader).items()})
        if "accounts" in raw:
            raw["accounts"] = [
                Account(w3.to_checksum_address(hex(account[0])), account[1])
                for account in raw["accounts"]
            ]
        return raw
