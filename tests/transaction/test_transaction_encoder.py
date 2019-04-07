from binance.crypto import *
from binance.environment import *
from binance.message import *
from binance.transaction import *

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

    expected_signature = b'44b2b9293ec4867fc2c77c822e13f090e8c6502ecbbc3349' \
                         b'af794e45c6fc8a9823728bcc3b482bf82b4a954f8a7bc198' \
                         b'1e1be4877b62311084c50fd95cae06ae'

    encoded_transaction = b'd901f0625dee0a65ce6dc0430a1454d41d0b0c4603cd932' \
                          b'605e61880abc2a2af7e25122b3534443431443042304334' \
                          b'36303343443933323630354536313838304142433241324' \
                          b'146374532352d31351a0b4e4e422d3237345f424e422002' \
                          b'2802308084af5f3880dea0cb054001126c0a26eb5ae9872' \
                          b'10216087947712ad02e55bf34a227974644f5a6cca39177' \
                          b'1b3868b495d62c5f7b1a124044b2b9293ec4867fc2c77c8' \
                          b'22e13f090e8c6502ecbbc3349af794e45c6fc8a9823728b' \
                          b'cc3b482bf82b4a954f8a7bc1981e1be4877b62311084c50' \
                          b'fd95cae06ae200e'

    wallet = create_test_wallet(sequence=14)

    encoder = TransactionEncoder(wallet)

    message = encoder.create_new_order_message(symbol="NNB-274_BNB",
                                               order_side=OrderSide.SELL,
                                               order_type=OrderType.LIMIT,
                                               price=200000000,
                                               quantity=1500000000,
                                               time_in_force=TimeInForce.GTE)

    assert binascii.hexlify(message.encode()) == encoded_msg

    signature = encoder.sign(message)

    assert binascii.hexlify(signature) == expected_signature

    transaction = encoder.create_transaction(message, signature)

    assert binascii.hexlify(transaction.encode()) == encoded_transaction
