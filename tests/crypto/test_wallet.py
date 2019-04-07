import binascii
from binance import *
from binance.crypto import *


def test_wallet():
    private_key = "95949f757db1f57ca94a5dff23314accbe7abee89597bf6a3c7382c84d7eb832"
    address = "tbnb1grpf0955h0ykzq3ar5nmum7y6gdfl6lx8xu7hm"
    public_key = b"eb5ae98721026a35920088d98c3888ca68c53dfc93f4564602606cbb87f0fe5ee533db38e502"

    wallet = Wallet(private_key, network=BinanceNetwork.TEST)

    assert wallet.address == address

    assert binascii.hexlify(wallet.public_key) == public_key
