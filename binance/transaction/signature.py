from binance.proto import ProtoObject, StdSignature


class Signature(ProtoObject):
    """
    Object that represents a signature.
    """

    def __init__(self,
                 public_key,
                 signature,
                 account_number,
                 sequence):
        """

        Args:
            public_key (bytes): The public key.
            signature(bytes): The signature.
            account_number (int): Another identifier of signer, which can be
                read from chain by account REST API or RPC
            sequence (int): Sequence number for the next transaction of the
                client, which can be read fro chain by account REST API or RPC.
        """
        super(Signature, self).__init__(
            StdSignature,
            prefix=b'',
            prepend_length=False
        )
        self.proto.pub_key = public_key
        self.proto.signature = signature
        self.proto.account_number = account_number
        self.proto.sequence = sequence
