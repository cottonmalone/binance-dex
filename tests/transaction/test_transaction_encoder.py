from binance.crypto import *
from binance.transaction import *
from binance.environment import *
from binance.model import *

MNEMONIC_PHRASE = "slot live best metal mandate page hover tank bronze code " \
                  "salad hill hen salad train inmate autumn nut home city " \
                  "shield level board measure"

PRIVATE_KEY = get_private_key_from_mnemonic(MNEMONIC_PHRASE)


def create_test_wallet(sequence):
    """
    Create wallet used for testing in this module.

    """
    # get wallet
    wallet = Wallet(PRIVATE_KEY, TEST_NET)

    # mock waller info
    wallet.account_number = 0
    wallet.sequence = sequence
    wallet.chain_id = "test-chain-n4b735"

    # double check to make sure wallet is valid
    assert wallet.address == "tbnb12n2p6zcvgcpumyexqhnp3q9tc2327l39ycfnyk"

    return wallet


def test_create_new_order_message():
    """
    Test function behaves as expected.
    """
    # expected values from Java SDK (sanity check)
    encoded_msg = b'ce6dc0430a1454d41d0b0c4603cd932605e61880abc2a2af7e25122' \
                  b'b353444343144304230433436303343443933323630354536313838' \
                  b'304142433241324146374532352d31351a0b4e4e422d3237345f424' \
                  b'e4220022802308084af5f3880dea0cb054001'

    wallet = create_test_wallet(sequence=14)

    encoder = TransactionEncoder(wallet)

    message = encoder.create_new_order_message(symbol="NNB-274_BNB",
                                               order_side=OrderSide.SELL,
                                               order_type=OrderType.LIMIT,
                                               price=200000000,
                                               quantity=1500000000,
                                               time_in_force=TimeInForce.GTE)

    assert binascii.hexlify(message.encode()) == encoded_msg
