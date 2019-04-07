import binascii
import pytest
from binance.crypto import *

"""
The following keys are taken from the Binance DEX SDK.
"""
PRIVATE_KEY = "30c5e838578a29e3e9273edddd753d6c9b38aca2446dd84bdfe2e5988b0da0a1"

MSG = "7b226163636f756e745f6e756d626572223a2231222c22636861696e5f6964223a22626e6" \
      "2636861696e2d31303030222c226d656d6f223a22222c226d736773223a5b7b226964223a" \
      "2242363536314443433130343133303035394137433038463438433634363130433146364" \
      "6393036342d3130222c226f7264657274797065223a322c227072696365223a3130303030" \
      "303030302c227175616e74697479223a313230303030303030302c2273656e646572223a2" \
      "2626e63316b6574706d6e71736779637174786e7570723667636572707073306b6c797279" \
      "687a36667a6c222c2273696465223a312c2273796d626f6c223a224254432d3543345f424" \
      "e42222c2274696d65696e666f726365223a317d5d2c2273657175656e6365223a2239227d"

SIGNATURE = "9c0421217ef92d556a14e3f442b07c85f6fc706dfcd8a72d6b58f05f96e95aa2" \
            "26b10f7cf62ccf7c9d5d953fa2c9ae80a1eacaf0c779d0253f1a34afd17eef34"


def test_generate_private_key():
    """
    Test function behaves as expected.
    """
    # just checking that the key is of expected length
    assert len(generate_private_key()) == 64


@pytest.mark.parametrize('key,prefix,address', [
    ("90335b9d2153ad1a9799a3ccc070bd64b4164e9642ee1dd48053c33f9a3a05e9",
     "tbnb",
     "tbnb1hgm0p7khfk85zpz5v0j8wnej3a90w709zzlffd"),
    ("90335b9d2153ad1a9799a3ccc070bd64b4164e9642ee1dd48053c33f9a3a05e9",
     "bnc",
     "bnc1hgm0p7khfk85zpz5v0j8wnej3a90w7098fpxyh")
])
def test_get_address_from_both_keys(key, prefix, address):
    """
    Test function behaves as expected.
    """
    # check that address is correct for private key
    assert get_address_from_private_key(key, prefix) == address

    # get public key from private key
    public_key = get_public_key_from_private_key(key)

    # check that address is correct for public key
    assert get_address_from_public_key(public_key, prefix) == address


def test_get_public_key_from_address():
    """
    Test function behaves as expected.
    """
    assert get_public_key_from_address(
        "tbnb1hgm0p7khfk85zpz5v0j8wnej3a90w709zzlffd"
    ) == "ba36f0fad74d8f41045463e4774f328f4af779e5"


def test_get_sender_address_in_bytes():
    """
    Test function behaves as expected.
    """
    assert get_sender_address_in_bytes(
        "tbnb1hgm0p7khfk85zpz5v0j8wnej3a90w709zzlffd"
    ) == binascii.unhexlify("ba36f0fad74d8f41045463e4774f328f4af779e5")


@pytest.mark.parametrize('private_key', [
    PRIVATE_KEY,
    get_private_key_from_hex(PRIVATE_KEY)
])
def test_generate_signature_for_message(private_key):
    """
    Test function behaves as expected.
    """
    # get binary message
    message_data = binascii.unhexlify(MSG)

    # generate signature
    signature = generate_signature_for_message(private_key,
                                               message_data)

    # verify that signature is correct
    assert binascii.hexlify(signature).decode() == SIGNATURE


@pytest.mark.parametrize('public_key', [
    get_public_key_from_private_key(PRIVATE_KEY),
    get_private_key_from_hex(PRIVATE_KEY).get_verifying_key()
])
def test_verify_signature_for_message(public_key):
    """
    Test function behaves as expected.
    """
    # get binary message
    message_data = binascii.unhexlify(MSG)

    # generate signature
    signature = binascii.unhexlify(SIGNATURE)

    # verify that signature is correct
    assert verify_signature_for_message(public_key, signature, message_data)

    # verify that bogus signature is rejected
    assert not verify_signature_for_message(public_key, signature, b'foo')
