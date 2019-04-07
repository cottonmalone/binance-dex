from binance import *
from binance.crypto import *
from binance.message import *
from binance.transaction import *

MNEMONIC_PHRASE = "slot live best metal mandate page hover tank bronze code " \
                  "salad hill hen salad train inmate autumn nut home city " \
                  "shield level board measure"

MNEMONIC_PHRASE_2 = "trial raw kiss bench silent crystal clever cloud " \
                    "chapter obvious error income mechanic attend army " \
                    "outer found cube tribe sort south possible scene fox"


def create_test_wallet_1(sequence):
    """
    Create wallet used for testing in this module.

    """
    private_key = get_private_key_from_mnemonic(
        "slot live best metal mandate page hover tank bronze code " \
        "salad hill hen salad train inmate autumn nut home city " \
        "shield level board measure"
    )

    # get wallet
    wallet = Wallet(private_key, BinanceNetwork.TEST)

    # mock waller info
    wallet.account_number = 0
    wallet.sequence = sequence
    wallet.chain_id = "test-chain-n4b735"

    # double check to make sure wallet is valid
    assert wallet.address == "tbnb12n2p6zcvgcpumyexqhnp3q9tc2327l39ycfnyk"

    return wallet


def create_test_wallet_2(sequence):
    """
    Create wallet used for testing in this module.

    """
    private_key = get_private_key_from_mnemonic(
        "trial raw kiss bench silent crystal clever cloud " \
        "chapter obvious error income mechanic attend army " \
        "outer found cube tribe sort south possible scene fox"
    )

    # get wallet
    wallet = Wallet(private_key, BinanceNetwork.TEST)

    # mock waller info
    wallet.account_number = 0
    wallet.sequence = sequence
    wallet.chain_id = "test-chain-n4b735"

    # double check to make sure wallet is valid
    assert wallet.address == "tbnb1mrslq6lhglm3jp7pxzlk8u4549pmtp9sgvn2rc"

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

    # create wallet
    wallet = create_test_wallet_1(sequence=14)

    # create encoder
    encoder = TransactionEncoder(wallet)

    # create message
    message = encoder.create_new_order_message(symbol="NNB-274_BNB",
                                               order_side=OrderSide.SELL,
                                               order_type=OrderType.LIMIT,
                                               price=200000000,
                                               quantity=1500000000,
                                               time_in_force=TimeInForce.GTE)

    # check message encoding is correct
    assert binascii.hexlify(message.encode()) == encoded_msg

    # create signature
    signature = encoder.sign(message)

    # check signature is correct
    assert binascii.hexlify(signature) == expected_signature

    # create transaction
    transaction = encoder.create_transaction(message, signature)

    # check transaction is correct
    assert binascii.hexlify(transaction.encode()) == encoded_transaction


def test_create_cancel_order_message():
    """
    Test function behaves as expected.
    """
    # expected values from Java SDK (sanity check)
    encoded_msg = b'166e681b0a1454d41d0b0c4603cd932605e61880abc2a2af7e25120' \
                  b'b4e4e422d3237345f424e421a2b3534443431443042304334363033' \
                  b'43443933323630354536313838304142433241324146374532352d3' \
                  b'134'

    expected_signature = b'c0d9a95bf30e74d0701e4033c419020dbbac4b282356183c' \
                         b'aba98af0d57fdc58c224c525d5669e28a2e8a3438312c6dc' \
                         b'5ea0c845eee224bb6080345086a9089a'

    encoded_transaction = b'c801f0625dee0a54166e681b0a1454d41d0b0c4603cd932' \
                          b'605e61880abc2a2af7e25120b4e4e422d3237345f424e42' \
                          b'1a2b3534443431443042304334363033434439333236303' \
                          b'54536313838304142433241324146374532352d3134126c' \
                          b'0a26eb5ae987210216087947712ad02e55bf34a22797464' \
                          b'4f5a6cca391771b3868b495d62c5f7b1a1240c0d9a95bf3' \
                          b'0e74d0701e4033c419020dbbac4b282356183caba98af0d' \
                          b'57fdc58c224c525d5669e28a2e8a3438312c6dc5ea0c845' \
                          b'eee224bb6080345086a9089a200e'

    # create wallet
    wallet = create_test_wallet_1(sequence=14)

    # create encoder
    encoder = TransactionEncoder(wallet)

    # create message
    message = encoder.create_cancel_order_message(
        ref_id="54D41D0B0C4603CD932605E61880ABC2A2AF7E25-14",
        symbol="NNB-274_BNB"
    )

    # check message encoding is correct
    assert binascii.hexlify(message.encode()) == encoded_msg

    # create signature
    signature = encoder.sign(message)

    # check signature is correct
    assert binascii.hexlify(signature) == expected_signature

    # create transaction
    transaction = encoder.create_transaction(message, signature)

    # check transaction is correct
    assert binascii.hexlify(transaction.encode()) == encoded_transaction


def test_create_token_freeze_message():
    """
    Test function behaves as expected.
    """
    # expected values from Java SDK (sanity check)
    encoded_msg = b'e774b32d0a14d8e1f06bf747f71907c130bf63f2b' \
                  b'4a943b584b012074e4e422d4333461880c2d72f'

    expected_signature = b'9ceabe0262a75b0da7556303580f56a094486cc9938a728f' \
                         b'903a57054061bd83cd77686043723a11f88bc20aeef3488a' \
                         b'f8514371bc074796c8e4f3c6469f007f'

    encoded_transaction = b'9c01f0625dee0a28e774b32d0a14d8e1f06bf747f71907c' \
                          b'130bf63f2b4a943b584b012074e4e422d4333461880c2d7' \
                          b'2f126c0a26eb5ae987210280ec8943329305e43b2e61127' \
                          b'28423ef9f9a7e7125621c3545c2f30ce08bf83c12409cea' \
                          b'be0262a75b0da7556303580f56a094486cc9938a728f903' \
                          b'a57054061bd83cd77686043723a11f88bc20aeef3488af8' \
                          b'514371bc074796c8e4f3c6469f007f2009'

    # create wallet
    wallet = create_test_wallet_2(sequence=9)

    # create encoder
    encoder = TransactionEncoder(wallet)

    # create message
    message = encoder.create_token_freeze_message(symbol="NNB-C3F",
                                                  amount=100000000)

    # check message encoding is correct
    assert binascii.hexlify(message.encode()) == encoded_msg

    # create signature
    signature = encoder.sign(message)

    # check signature is correct
    assert binascii.hexlify(signature) == expected_signature

    # create transaction
    transaction = encoder.create_transaction(message, signature)

    # check transaction is correct
    assert binascii.hexlify(transaction.encode()) == encoded_transaction


def test_create_token_unfreeze_message():
    """
    Test function behaves as expected.
    """
    # expected values from Java SDK (sanity check)
    encoded_msg = b'6515ff0d0a14d8e1f06bf747f71907c130bf63f2' \
                  b'b4a943b584b012074e4e422d4333461880c2d72f'

    expected_signature = b'9ceabe0262a75b0da7556303580f56a094486cc9938a728f' \
                         b'903a57054061bd83cd77686043723a11f88bc20aeef3488a' \
                         b'f8514371bc074796c8e4f3c6469f007f'

    encoded_transaction = b'9c01f0625dee0a286515ff0d0a14d8e1f06bf747f71907c' \
                          b'130bf63f2b4a943b584b012074e4e422d4333461880c2d7' \
                          b'2f126c0a26eb5ae987210280ec8943329305e43b2e61127' \
                          b'28423ef9f9a7e7125621c3545c2f30ce08bf83c12409cea' \
                          b'be0262a75b0da7556303580f56a094486cc9938a728f903' \
                          b'a57054061bd83cd77686043723a11f88bc20aeef3488af8' \
                          b'514371bc074796c8e4f3c6469f007f2009'

    # create wallet
    wallet = create_test_wallet_2(sequence=9)

    # create encoder
    encoder = TransactionEncoder(wallet)

    # create message
    message = encoder.create_token_unfreeze_message(symbol="NNB-C3F",
                                                    amount=100000000)

    # check message encoding is correct
    assert binascii.hexlify(message.encode()) == encoded_msg

    # create signature
    signature = encoder.sign(message)

    # check signature is correct
    assert binascii.hexlify(signature) == expected_signature

    # create transaction
    transaction = encoder.create_transaction(message, signature)

    # check transaction is correct
    assert binascii.hexlify(transaction.encode()) == encoded_transaction


def test_create_transfer_message():
    """
    Test function behaves as expected.
    """
    # expected values from Java SDK (sanity check)

    recipient = "tbnb1rqa5gxmgzjhepvkhdtvkuxd4yqyv2w7sm8p78g"
    encoded_msg = b'2a2c87fa0a220a1454d41d0b0c4603cd932605e61880abc2a2af7e25120a0a03424e421080c2d72f12220a14183b441b6814af90b2d76ad96e19b52008c53bd0120a0a03424e421080c2d72f'

    expected_signature = b'8ad9bc7fd3ebf41a1a8874d643873affdc3ef77cb40cfba72795815574b4cc72f2310f25baa504326846308f277134dfb4a8cbf5fab9c6146d204a95d5e1056b'

    encoded_transaction = b'c001f0625dee0a4c2a2c87fa0a220a1454d41d0b0c4603cd932605e61880abc2a2af7e25120a0a03424e421080c2d72f12220a14183b441b6814af90b2d76ad96e19b52008c53bd0120a0a03424e421080c2d72f126c0a26eb5ae987210216087947712ad02e55bf34a227974644f5a6cca391771b3868b495d62c5f7b1a12408ad9bc7fd3ebf41a1a8874d643873affdc3ef77cb40cfba72795815574b4cc72f2310f25baa504326846308f277134dfb4a8cbf5fab9c6146d204a95d5e1056b200b'

    # create wallet
    wallet = create_test_wallet_1(sequence=11)

    # create encoder
    encoder = TransactionEncoder(wallet)

    # create message
    message = encoder.create_transfer_message(coin="BNB",
                                              amount=100000000,
                                              recipient_address=recipient)

    # check message encoding is correct
    assert binascii.hexlify(message.encode()) == encoded_msg

    # create signature
    signature = encoder.sign(message)

    # check signature is correct
    assert binascii.hexlify(signature) == expected_signature

    # create transaction
    transaction = encoder.create_transaction(message, signature)

    # check transaction is correct
    assert binascii.hexlify(transaction.encode()) == encoded_transaction


def test_create_vote_message():
    """
    Test function behaves as expected.
    """
    # expected values from Java SDK (sanity check)
    encoded_msg = b'a1cadd3608db021214d8e1f06bf' \
                  b'747f71907c130bf63f2b4a943b584b01801'

    expected_signature = b'37f4f39cf414461c478f166a2d59705dd8566fd573214c5c' \
                         b'002a075d6a6d86c237d6f237c35983d001e4b322b1d0f9ce' \
                         b'f9328d670f163600e3af2226792c4b16'

    encoded_transaction = b'9301f0625dee0a1fa1cadd3608db021214d8e1f06bf747f' \
                          b'71907c130bf63f2b4a943b584b01801126c0a26eb5ae987' \
                          b'210280ec8943329305e43b2e6112728423ef9f9a7e71256' \
                          b'21c3545c2f30ce08bf83c124037f4f39cf414461c478f16' \
                          b'6a2d59705dd8566fd573214c5c002a075d6a6d86c237d6f' \
                          b'237c35983d001e4b322b1d0f9cef9328d670f163600e3af' \
                          b'2226792c4b162009'

    # create wallet
    wallet = create_test_wallet_2(sequence=9)

    # create encoder
    encoder = TransactionEncoder(wallet)

    # create message
    message = encoder.create_vote_message(proposal_id=347,
                                          option_set=VoteOption.Yes)

    # check message encoding is correct
    assert binascii.hexlify(message.encode()) == encoded_msg

    # create signature
    signature = encoder.sign(message)

    # check signature is correct
    assert binascii.hexlify(signature) == expected_signature

    # create transaction
    transaction = encoder.create_transaction(message, signature)

    # check transaction is correct
    assert binascii.hexlify(transaction.encode()) == encoded_transaction
