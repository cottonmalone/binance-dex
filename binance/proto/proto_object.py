

class ProtoObject(object):
    """
    Base class that encapsulate the proto object and provides methods to encode.
    """

    def __init__(self, proto_class, prefix, prepend_length):
        """

        Args:
            proto_class (class): The protobuffer class.
            prefix (bytes): The prefix for object.
            prepend_length (bool): Whether the length of the object should be
                prepended to the encoded form.
        """
        self.proto = proto_class()
        self.prefix = prefix
        self.prepend_length = prepend_length

    @staticmethod
    def encode_uint(value):
        """
        Encode variable unsigned integer to byte (as VarInt).

        Args:
            value (int): The value to encode.

        Returns:
            bytes: The encoded value.

        """
        buffer = b''
        shifted_value = True
        while shifted_value:
            shifted_value = value >> 7
            buffer += bytes(
                ((value & 0x7F) | (0x80 if shifted_value != 0 else 0x00),))
            value = shifted_value
        return buffer

    def encode(self):
        """
        Encode object using Google protobuffer.

        Returns:
            bytes: The encoded object as bytes.

        """
        buffer = b''

        # prepend message length if needed
        if self.prepend_length:
            buffer += ProtoObject.encode_uint(
                len(self.prefix) + self.proto.ByteSize())

        # add object prefix and content
        buffer += self.prefix + bytes(self.proto.SerializeToString())

        return buffer



