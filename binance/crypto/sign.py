import collections
import binascii
import json
from google.protobuf.json_format import MessageToDict as msg_to_dict

SignData = collections.namedtuple("SignData", [
    'chain_id',
    'account_number',
    'sequence',
    'memo',
    'msgs',
    'source',
    'data'
])


def get_data_from_messages(msgs):
    return [msg.to_dict()
            for msg in msgs]


def get_sign_data(wallet, msgs, memo, source, data):
    return SignData(chain_id=wallet.chain_id,
                    account_number=wallet.account_number,
                    sequence=wallet.sequence,
                    msgs=get_data_from_messages(msgs),
                    memo=memo,
                    source=source,
                    data=data)


def get_json_bytes_for_sign_data(sign_data):
    return json.dumps(sign_data._asdict(),
                      sort_keys=True,
                      separators=(',', ':')).encode()
