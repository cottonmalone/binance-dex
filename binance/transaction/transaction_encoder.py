import binascii
from .new_order_message import *


class TransactionEncoder(object):

    def __init__(self, wallet, memo="", source=0, data=None):
        self.wallet = wallet
        self.memo = memo
        self.source = source
        self.data = data

    def create_new_order_message(self,
                                 symbol,
                                 order_type,
                                 order_side,
                                 price,
                                 quantity,
                                 time_in_force):
        """

        Args:
            symbol (str): Symbol for trading pair in full name of the tokens
            order_type (OrderType): The order type
            order_side (OrderSide): The order side.
            price (int): Price of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer
            quantity (int): Quantity of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer
            time_in_force (TimeInForce): The time in force.

        Returns:
            NewOrderMessage: The created message object.

        """
        # get compressed address
        address = binascii.hexlify(self.wallet.address_in_bytes).decode()

        # create order ID from compressed address and sequence ID
        order_id = address.upper() + '-' + str(self.wallet.sequence + 1)

        return NewOrderMessage(
            id=order_id,
            sender=self.wallet.address,
            symbol=symbol,
            order_type=order_type.value,
            side=order_side.value,
            price=price,
            quantity=quantity,
            time_in_force=time_in_force.value
        )
