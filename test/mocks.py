class MockedAccount:
    def __init__(self):
        self._enabled_hd_wallet = False

    def enable_unaudited_hdwallet_features(self):
        self._enabled_hd_wallet = True

    async def sign_transaction(self, txn, private_key: str):
        return txn


class MockedEth:
    def __init__(self) -> None:
        self._account = MockedAccount()

    @property
    async def chain_id(self):
        return 1

    @property
    def account(self):
        return self._account

    async def get_transaction_count(self, _: str):
        return 1

    async def send_raw_transaction(self, _: str):
        return "test_hash"


class MockedProvider:
    def __init__(self, url: str):
        self._url = url


class MockedWeb3:
    AsyncHTTPProvider = MockedProvider

    def __init__(self, _: MockedProvider):
        self._eth = MockedEth()

    @property
    def eth(self):
        return self._eth

    def to_hex(self, data: bytes) -> str:
        return data.hex()

    def keccak(self, _: str) -> bytes:
        return b"0"
