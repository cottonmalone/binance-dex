import collections
from enum import Enum

Network = collections.namedtuple('Network', [
    'api_url',
    'ws_url',
    'hrp'
])


class BinanceNetwork(Enum):
    PRODUCTION = Network(
        api_url="https://dex.binance.org",
        ws_url="wss://dex.binance.org/api/",
        hrp="bnb"
    )
    TEST = Network(
        api_url="https://testnet-dex.binance.org",
        ws_url="wss://testnet-dex.binance.org/api/",
        hrp="tbnb"
    )
