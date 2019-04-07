import binance.crypto
from binance.proto import ProtoObject, NewOrder


class NewOrderMessage(ProtoObject):
    """
    Object that represents a new order.
    """

    def __init__(self,
                 id,
                 sender,
                 symbol,
                 order_type,
                 order_side,
                 price,
                 quantity,
                 time_in_force):
        """

        Args:
            id (str): The order ID.
            sender (str): The originating address.
            symbol (str): Symbol for trading pair in full name of the tokens.
            order_type (OrderType): The order type.
            order_side (OrderSide): The order side.
            price (int): Price of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer.
            quantity (int): Quantity of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer.
            time_in_force (TimeInForce): The time in force.

        """
        super(NewOrderMessage, self).__init__(
            NewOrder,
            prefix=b'\xcem\xc0C',
            prepend_length=False
        )
        self.proto.id = id
        self.sender_address = sender
        self.proto.sender = binance.crypto.get_sender_address_in_bytes(
            sender)
        self.proto.symbol = symbol
        self.proto.ordertype = order_type.value
        self.proto.side = order_side.value
        self.proto.price = price
        self.proto.quantity = quantity
        self.proto.timeinforce = time_in_force.value

    def to_dict(self):
        dict = super(NewOrderMessage, self).to_dict()

        dict["sender"] = self.sender_address

        return dict
