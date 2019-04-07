from binance.proto import ProtoObject, StdTx


class Transaction(ProtoObject):
    """
    Object that represents a transaction to be broadcasted.
    """

    def __init__(self, memo="", source=0, data=b''):
        """

        Args:
            memo (str): A short sentence of remark for the transaction.
            source (int). The transaction source.
            data (bytes): Additional data (Reserved for future use).
        """
        super(Transaction, self).__init__(
            StdTx,
            prefix=b'\xf0b]\xee',
            prepend_length=True
        )
        self.proto.memo = memo
        self.proto.source = source
        self.proto.data = data

    def add_message(self, message):
        """
        Add message to transaction.

        Args:
            message (MessageObject): The message.

        """
        self.proto.msgs.extend([message.encode()])

    def add_signature(self, signature):
        """
        Add signature to transaction.

        Args:
            signature (Signature): The signature.

        """
        self.proto.signatures.extend([signature.encode()])
