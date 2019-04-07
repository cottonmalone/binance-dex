import binascii
import collections
import json

SignData = collections.namedtuple("SignData", [
    'chain_id',
    'account_number',
    'sequence',
    'memo',
    'msgs',
    'source',
    'data'
])
"""
Structure to store sign data information.
"""


def get_sign_data(wallet, msgs, memo, source, data):
    """
    Create sign data for messages.

    Args:
        wallet (Wallet): The wallet for the sign data.
        msgs (list): A list of messages to be signed.
        memo (str): The memo for the transaction.
        source (int): The source for the transaction.
        data (bytes): Additional data.

    Returns:
        SignData: The sign data object.

    """
    return SignData(chain_id=wallet.chain_id,
                    account_number=str(wallet.account_number),
                    sequence=str(wallet.sequence),
                    msgs=[msg.to_dict() for msg in msgs],
                    memo=memo,
                    source=str(source),
                    data=data)


def get_json_bytes_for_sign_data(sign_data):
    """
    Convert SignData object to JSON bytes for signing.

    Args:
        sign_data (SignData): The sign data object.

    Returns:
        bytes: The sign data in JSON bytes.

    """
    return json.dumps(sign_data._asdict(),
                      sort_keys=True,
                      separators=(',', ':')).encode()
