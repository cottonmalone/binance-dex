from binance.crypto import *
from binance.message import *
from binance.transaction import *


def test_get_json_bytes_for_sign_data():
    """
    Test function behaves as expected.
    """
    # expected values from Java SDK (sanity check)
    encoded_json = b"7b226163636f756e745f6e756d626572223a223132222c2263686169" \
                   b"6e5f6964223a22636861696e2d626e62222c2264617461223a6e756c" \
                   b"6c2c226d656d6f223a22222c226d736773223a5b7b226964223a2242" \
                   b"41333646304641443734443846343130343534363345343737344633" \
                   b"32384634414637373945352d3336222c226f7264657274797065223a" \
                   b"322c227072696365223a3133363335303030302c227175616e746974" \
                   b"79223a3130303030303030302c2273656e646572223a22626e633168" \
                   b"676d3070376b68666b38357a707a3576306a38776e656a3361393077" \
                   b"373039386670787968222c2273696465223a312c2273796d626f6c22" \
                   b"3a224e4e422d3333385f424e42222c2274696d65696e666f72636522" \
                   b"3a317d5d2c2273657175656e6365223a223335222c22736f75726365" \
                   b"223a2231227d"
    private_key = "90335b9d2153ad1a9799a3ccc070bd64" \
                  "b4164e9642ee1dd48053c33f9a3a05e9"
    expected_signature = b"08bf9c556c1f632e42c4eca3efd72971517a07b07853af3d8" \
                         b"f8581ee58209a9771763286cf2859b62c6e3f139ac15c3d46" \
                         b"eafd7b1d71763ac45a4b053b23a347"

    # create new order message
    msg = NewOrderMessage(
        sender="bnc1hgm0p7khfk85zpz5v0j8wnej3a90w7098fpxyh",
        id="BA36F0FAD74D8F41045463E4774F328F4AF779E5-36",
        symbol="NNB-338_BNB",
        order_type=2,
        side=1,
        price=136350000,
        quantity=100000000,
        time_in_force=1)

    # get sign data with message
    sign_data = SignData(chain_id='chain-bnb',
                         account_number='12',
                         sequence='35',
                         memo='',
                         msgs=[msg.to_dict()],
                         source='1',
                         data=None)

    # encode JSON to bytes
    encoded_message = get_json_bytes_for_sign_data(sign_data)

    # check that it matches expected
    assert encoded_json == binascii.hexlify(encoded_message)

    # get signature
    signature = generate_signature_for_message(private_key, encoded_message)

    # verify that signature matches expected
    assert binascii.hexlify(signature) == expected_signature
