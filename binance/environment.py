import collections

Environment = collections.namedtuple('Environment', [
    'url',
    'ws_url',
    'hrp'
])

PRODUCTION = Environment(
    url="https://dex.binance.org",
    ws_url="wss://dex.binance.org/api/",
    hrp="bnb"
)

TEST_NET = Environment(
    url="https://testnet-dex.binance.org",
    ws_url="wss://testnet-dex.binance.org/api/",
    hrp="tbnb"
)
