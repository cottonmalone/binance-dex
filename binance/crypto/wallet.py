from .keys import *


class Wallet(object):

    def __init__(self, private_key, environment):
        self.private_key = get_private_key_from_hex(private_key)

        self.environment = environment

        self.public_key = binascii.unhexlify(
            "eb5ae98721" + get_public_key_from_private_key(private_key)
        )

        self.address = get_address_from_private_key(private_key,
                                                    environment.hrp)

        self.account_number = None
        self.sequence = None
        self.chain_id = None

    def init_account(self, client):
        raise NotImplementedError()

    def init_chain_id(self, client):
        raise NotImplementedError()

    def reload_sequence(self, client):
        raise NotImplementedError()
