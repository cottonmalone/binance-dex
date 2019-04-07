import binance.crypto
from binance.proto import ProtoObject, Vote
from .constants import VoteOption

class VoteMessage(ProtoObject):
    """
    Object that represents a vote message.
    """

    def __init__(self,
                 voter,
                 proposal_id,
                 option_set):
        """

        Args:
            voter (str): The voter's address.
            proposal_id (int): The ID of the proposal.
            option_set (VoteOption): The vote option.

        """
        super(VoteMessage, self).__init__(
            Vote,
            prefix=b'\xa1\xca\xdd6',
            prepend_length=False
        )
        self.sender_address = voter
        self.proto.voter = binance.crypto.get_sender_address_in_bytes(
            voter)
        self.proto.proposal_id = proposal_id
        self.proto.option = option_set.value

    def to_dict(self):
        # call base method
        dict = super(VoteMessage, self).to_dict()

        # override JSON translation to handle corner case for sender
        dict["voter"] = self.sender_address
        dict["proposal_id"] = str(dict["proposal_id"])
        dict['option'] = VoteOption(dict['option']).name

        return dict
