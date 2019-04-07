import binascii
import binance.crypto
import binance.message
from .signature import *
from .transaction import *


class TransactionEncoder(object):

    def __init__(self, wallet, memo="", source=0, data=None):
        self.wallet = wallet
        self.memo = memo
        self.source = source
        self.data = data

    def sign(self, message):
        """
        Sign message.

        Args:
            message (Message): The message to sign.

        Returns:
            bytes: The message signature.

        """
        # get sign data with message
        sign_data = binance.crypto.get_sign_data(wallet=self.wallet,
                                                 msgs=[message],
                                                 memo=self.memo,
                                                 source=self.source,
                                                 data=self.data)

        # sign encoded JSON to bytes
        return binance.crypto.generate_signature_for_message(
            self.wallet.private_key,
            binance.crypto.get_json_bytes_for_sign_data(sign_data)
        )

    def create_transaction(self, message, signature):
        transaction = Transaction(memo=self.memo,
                                  source=self.source,
                                  data=b'' if self.data is None else self.data)

        transaction.add_message(message)
        transaction.add_signature(Signature(public_key=self.wallet.public_key,
                                            signature=signature,
                                            account_number=self.wallet.account_number,
                                            sequence=self.wallet.sequence))

        return transaction

    def create_new_order_message(self,
                                 symbol,
                                 order_type,
                                 order_side,
                                 price,
                                 quantity,
                                 time_in_force):
        """
        Create New Order Message from parameters.

        Args:
            symbol (str): Symbol for trading pair in full name of the tokens.
            order_type (OrderType): The order type.
            order_side (OrderSide): The order side.
            price (int): Price of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer.
            quantity (int): Quantity of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer.
            time_in_force (TimeInForce): The time in force.

        Returns:
            NewOrderMessage: The created message object.

        """
        # get compressed address
        address = binascii.hexlify(self.wallet.address_in_bytes).decode()

        # create order ID from compressed address and sequence ID
        order_id = address.upper() + '-' + str(self.wallet.sequence + 1)

        return binance.message.NewOrderMessage(
            id=order_id,
            sender=self.wallet.address,
            symbol=symbol,
            order_type=order_type,
            order_side=order_side,
            price=price,
            quantity=quantity,
            time_in_force=time_in_force
        )
