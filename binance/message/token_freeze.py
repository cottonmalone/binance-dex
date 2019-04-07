import binance.crypto
from binance.proto import ProtoObject, TokenFreeze


class TokenFreezeMessage(ProtoObject):
    """
    Object that represents a token freeze message.
    """

    def __init__(self,
                 sender,
                 symbol,
                 amount):
        """

        Args:
            sender (str): The originating address.
            symbol (str): Symbol for trading pair in full name of the tokens.
            amount (int): The amount of tokens to freeze.

        """
        super(TokenFreezeMessage, self).__init__(
            TokenFreeze,
            prefix=b'\xe7t\xb3-',
            prepend_length=False
        )
        self.sender_address = sender
        setattr(self.proto, "from", binance.crypto.get_sender_address_in_bytes(
            sender))
        self.proto.symbol = symbol
        self.proto.amount = amount

    def to_dict(self):
        # call base method
        dict = super(TokenFreezeMessage, self).to_dict()

        # override JSON translation to handle corner case for sender
        dict["from"] = self.sender_address

        return dict
