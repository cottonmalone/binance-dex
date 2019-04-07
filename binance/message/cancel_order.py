import binance.crypto
from binance.proto import ProtoObject, CancelOrder


class CancelOrderMessage(ProtoObject):
    """
    Object that represents a cancel order message.
    """

    def __init__(self,
                 sender,
                 symbol,
                 ref_id):
        """

        Args:
            sender (str): The originating address.
            symbol (str): Symbol for trading pair in full name of the tokens.
            ref_id (str): The order ID of the one to cancel.

        """
        super(CancelOrderMessage, self).__init__(
            CancelOrder,
            prefix=b'\x16nh\x1b',
            prepend_length=False
        )
        self.sender_address = sender
        self.proto.sender = binance.crypto.get_sender_address_in_bytes(
            sender)
        self.proto.symbol = symbol
        self.proto.refid = ref_id

    def to_dict(self):
        # call base method
        dict = super(CancelOrderMessage, self).to_dict()

        # override JSON translation to handle corner case for sender
        dict["sender"] = self.sender_address

        return dict
