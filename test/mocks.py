class MockedAccount:
    def __init__(self):
        self._enabled_hd_wallet = False

    def enable_unaudited_hdwallet_features(self):
        self._enabled_hd_wallet = True


class MockedEth:
    def __init__(self) -> None:
        self._account = MockedAccount()

    @property
    async def chain_id(self):
        return 1

    @property
    def account(self):
        return self._account


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
