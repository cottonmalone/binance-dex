import binascii
import bitcoin
import ecdsa
import hashlib
import cryptos
from binance.utils import segwit_addr

def get_private_key_from_hex(hex):
    """
    Get private key from hexadecimal representation.

    Args:
        hex (str): The hexadecimal string.

    Returns:
        ecdsa.SigningKey: The private key.

    """
    return ecdsa.SigningKey.from_string(binascii.unhexlify(hex),
                                        curve=ecdsa.SECP256k1)


def get_hex_from_private_key(key):
    """
    Get hexadecimal representation of private key.

    Args:
        key (ecdsa.SigningKey): The private key.

    Returns:
        str: The hexadecimal string.

    """
    return binascii.hexlify(key.to_string()).decode()


def get_public_key_from_hex(hex):
    """
    Get public key from hexadecimal representation.

    Args:
        hex (str): The hexadecimal string.

    Returns:
        ecdsa.VerifyingKey: The primary key.

    """
    return ecdsa.VerifyingKey.from_string(
        bitcoin.decompress(binascii.unhexlify(hex))[1:],
        curve=ecdsa.SECP256k1
    )


def get_hex_from_public_key(key):
    """
    Get hexadecimal representation of public key.

    Args:
        key (ecdsa.VerifyingKey): The public key.

    Returns:
        str: The hexadecimal string.

    """
    return bitcoin.compress('04' + binascii.hexlify(key.to_string()).decode())


def generate_private_key():
    """
    Generate random private key.

    Returns:
        str: The hexadecimal representation of the key.

    """
    return get_hex_from_private_key(
        ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    )


def get_public_key_from_private_key(private_key):
    """
    Get public key from private key.

    Args:
        private_key (str): The hexadecimal representation of the key.

    Returns:
        str: The corresponding public key in hexadecimal form.

    """
    return get_hex_from_public_key(
        get_private_key_from_hex(private_key).get_verifying_key()
    )


def get_address_from_public_key(public_key, prefix="tbnb"):
    """
    Get address from public key.

    Args:
        public_key (str): The public key in hexadecimal form.
        prefix (str): The address prefix

    Returns:
        str: The hexadecimal representation of the address.

    """
    # get compressed public key (33 bytes from 64)
    # compressed_key = bitcoin.compress('04' + public_key)

    # get sha256 hash
    sha256 = hashlib.sha256(binascii.unhexlify(public_key.encode())).digest()

    # get ripemd160 hash
    ripemd160 = hashlib.new('ripemd160', sha256).digest()

    # convert digest to bytes
    data = segwit_addr.convertbits(ripemd160, 8, 5)

    # encode using segwit_addr library
    return segwit_addr.bech32_encode(prefix, data)


def get_public_key_from_address(address):
    """
    Get public key from address.

    Args:
        address (str): The hexadecimal representation of the address.

    Returns:
        str: The public key in hexadecimal form.

    """
    # get address data
    _, data = segwit_addr.bech32_decode(address)

    # decode data back to key
    decoded = segwit_addr.convertbits(data, 5, 8, False)

    # convert byte array to hex
    public_key = binascii.hexlify(bytearray(decoded)).decode()

    return public_key


def get_address_from_private_key(private_key, prefix="tbnb"):
    """
    Get address from public key.

    Args:
        private_key (str): The private key in hexadecimal form.
        prefix (str): The address prefix (e.g. bnb or tbnb).

    Returns:
        str: The hexadecimal representation of the address.

    """
    return get_address_from_public_key(
        get_public_key_from_private_key(private_key),
        prefix
    )


def get_sender_address_in_bytes(address):
    """
    Get sender address in bytes form.

    Args:
        address (str): The address.

    Returns:
        bytes: The address in bytes form.

    """
    return binascii.unhexlify(get_public_key_from_address(address))


def generate_signature_for_message(private_key, message):
    """
    Generate signature for message.

    Args:
        private_key (str): The private key in hexadecimal form.
        message (bytes): The message to sign in bytes.

    Returns:
        bytes: The signed message.

    """
    # get private key
    key = get_private_key_from_hex(private_key)

    # sign message using sha256
    return key.sign_deterministic(message, hashfunc=hashlib.sha256)


def verify_signature_for_message(public_key, signature, message):
    """
    Verify signature for message.

    Args:
        public_key (str): The public key in hexadecimal form.
        signature (bytes): The message to sign in bytes.
        message (bytes): The message to sign in bytes.

    Returns:
        bool: Whether the signature was verified.

    """
    key = get_public_key_from_hex(public_key)

    # this function is annoying as it will return True if verified but
    # an exception if not, not very good application of good design principles
    try:
        return key.verify(signature, message, hashfunc=hashlib.sha256)
    except ecdsa.BadSignatureError:
        return False
