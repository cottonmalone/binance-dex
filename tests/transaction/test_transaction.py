from binance.transaction import *
import binascii


def test_new_order_message():
    """
    Test function behaves as expected.
    """
    # test parameters
    sender = "b6561dcc104130059a7c08f48c64610c1f6f9064"
    public_key = "eb5ae9872103baf53d1424f8ea83d03a82f6d1" \
                 "57b5401c4ea57ffb8317872e15a19fc9b7ad7b"
    signature = "e79a6606d28cf07b9cc6f566b524a5282b13beccc3162376c79f39262" \
                "0c95a447b19f64e761e22a7a3bc311a780e7d9fdd521e2f7edec25308" \
                "c5bac6aa1c0a31"
    encoded_transaction = "db01f0625dee0a65ce6dc0430a14b6561dcc104130059a7" \
                          "c08f48c64610c1f6f9064122b4236353631444343313034" \
                          "31333030353941374330384634384336343631304331463" \
                          "646393036342d31311a0b4254432d3543345f424e422002" \
                          "28013080c2d72f3880989abc044001126e0a26eb5ae9872" \
                          "103baf53d1424f8ea83d03a82f6d157b5401c4ea57ffb83" \
                          "17872e15a19fc9b7ad7b1240e79a6606d28cf07b9cc6f56" \
                          "6b524a5282b13beccc3162376c79f392620c95a447b19f6" \
                          "4e761e22a7a3bc311a780e7d9fdd521e2f7edec25308c5b" \
                          "ac6aa1c0a311801200a"

    # create transcation
    transaction = Transaction()

    # add new order message
    transaction.add_message(
        NewOrderMessage(sender=binascii.unhexlify(sender),
                        id="B6561DCC104130059A7C08F48C64610C1F6F9064-11",
                        symbol="BTC-5C4_BNB",
                        order_type=2,
                        side=1,
                        price=100000000,
                        quantity=1200000000,
                        time_in_force=1)
    )

    # sign message
    transaction.add_signature(
        Signature(public_key=binascii.unhexlify(public_key),
                  signature=binascii.unhexlify(signature),
                  account_number=1,
                  sequence=10)
    )

    # check that the encoded transaction matches expected
    assert binascii.hexlify(transaction.encode()).decode() == \
           encoded_transaction
