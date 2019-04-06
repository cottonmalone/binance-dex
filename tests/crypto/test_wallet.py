import binascii
from binance.crypto import *
from binance.environment import TEST_NET


def test_wallet():
    private_key = "95949f757db1f57ca94a5dff23314accbe7abee89597bf6a3c7382c84d7eb832"
    address = "tbnb1grpf0955h0ykzq3ar5nmum7y6gdfl6lx8xu7hm"
    address_in_bytes = b"40c2979694bbc961023d1d27be6fc4d21a9febe6"
    public_key = b"eb5ae98721026a35920088d98c3888ca68c53dfc93f4564602606cbb87f0fe5ee533db38e502"

    wallet = Wallet(private_key, environment=TEST_NET)

    assert wallet.address == address
    assert binascii.hexlify(wallet.address_in_bytes) == address_in_bytes

    assert binascii.hexlify(wallet.public_key) == public_key
