import binascii
import binance.crypto
from binance.proto import ProtoObject, Send


class TransferMessage(ProtoObject):
    """
    Object that represents a transfer message.
    """

    def __init__(self,
                 coin,
                 amount,
                 sender_address,
                 recipient_address):
        """

        Args:
            coin (str): The coin symbol (e.g. BTC, ETH, BNB, etc.).
            amount (int): The amount of tokens to transfer.
            sender_address (str): The sender's address.
            recipient_address (str): The recipient's address.

        """
        super(TransferMessage, self).__init__(
            Send,
            prefix=b'*,\x87\xfa',
            prepend_length=False
        )
        self.sender_address = sender_address
        self.recipient_address = recipient_address

        token = Send.Token()
        token.denom = coin
        token.amount = amount

        input = self.proto.inputs.add()
        input.address = binance.crypto.get_address_in_bytes(sender_address)
        input.coins.extend([token])

        output = self.proto.outputs.add()
        output.address = binance.crypto.get_address_in_bytes(recipient_address)
        output.coins.extend([token])

    def to_dict(self):
        # call base method
        dict = super(TransferMessage, self).to_dict()

        # override JSON translation to handle corner case for sender
        dict["inputs"][0]["address"] = self.sender_address
        dict["outputs"][0]["address"] = self.recipient_address
        dict["inputs"][0]["coins"][0]["amount"] = \
            int(dict["inputs"][0]["coins"][0]["amount"])
        dict["outputs"][0]["coins"][0]["amount"] = \
            int(dict["outputs"][0]["coins"][0]["amount"])

        return dict
