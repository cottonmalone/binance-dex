from binance.proto import ProtoObject, NewOrder

"""
message NewOrder {
    //    0xCE6DC043 // hardcoded, object type prefix in 4 bytes
    bytes sender = 1; // order originating address
    string id = 2; // order id, optional
    string symbol = 3; // symbol for trading pair in full name of the tokens
    int64 ordertype = 4; // only accept 2 for now, meaning limit order
    int64 side = 5; // 1 for buy and 2 fory sell
    int64 price = 6; // price of the order, which is the real price multiplied by 1e8 (10^8) and rounded to integer
    int64 quantity = 7; // quantity of the order, which is the real price multiplied by 1e8 (10^8) and rounded to integer
    int64 timeinforce = 8; // 1 for Good Till Expire(GTE) order and 3 for Immediate Or Cancel (IOC)
}"""


class NewOrderMessage(ProtoObject):
    """
    Object that represents a new order.
    """

    def __init__(self,
                 id,
                 sender,
                 symbol,
                 order_type,
                 side,
                 price,
                 quantity,
                 time_in_force):
        """

        Args:
            id (str): The order ID.
            sender (bytes): The originating address.
            symbol (str): Symbol for trading pair in full name of the tokens
            order_type (int): Only accept 2 for now, meaning limit order.
            side (int): 1 for buy and 2 fory sell
            price (int): Price of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer
            quantity (int): Quantity of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer
            time_in_force (int): 1 for Good Till Expire(GTE) order and 3 for
                Immediate Or Cancel (IOC)
        """
        super(NewOrderMessage, self).__init__(
            NewOrder,
            prefix=b'\xcem\xc0C',
            prepend_length=False
        )
        self.proto.id = id
        self.proto.sender = sender
        self.proto.symbol = symbol
        self.proto.ordertype = order_type
        self.proto.side = side
        self.proto.price = price
        self.proto.quantity = quantity
        self.proto.timeinforce = time_in_force
        self.proto.msgType: "NewOrderMsg"
