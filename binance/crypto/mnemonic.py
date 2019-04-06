import cryptos
import binance.utils.bip32

HDPATH = "44'/714'/0'/0/0"

def get_private_key_from_mnemonic(phrase):
    """
    Get private key from mnemonic phrase.

    Args:
        phrase (str): The 24 work mnemonic phase.

    Returns:
        str: The private key in hexadecimal form.

    """
    # get seed from BIP 39 phrase
    seed = cryptos.mnemonic_to_seed(phrase)

    # generate master key using BIP 32
    key = binance.utils.bip32.bip32_master_key(seed)

    # get derived key from HD path
    return binance.utils.bip32.bip32_derive_key(key, HDPATH)[:-2]
