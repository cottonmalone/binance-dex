import binascii
import binance.crypto
import binance.message
from .signature import *
from .transaction import *


class TransactionEncoder(object):

    def __init__(self, wallet, memo="", source=0, data=None):
        self.wallet = wallet
        self.memo = memo
        self.source = source
        self.data = data

    def sign(self, message):
        """
        Sign message.

        Args:
            message (Message): The message to sign.

        Returns:
            bytes: The message signature.

        """
        # get sign data with message
        sign_data = binance.crypto.get_sign_data(wallet=self.wallet,
                                                 msgs=[message],
                                                 memo=self.memo,
                                                 source=self.source,
                                                 data=self.data)

        print(binance.crypto.get_json_bytes_for_sign_data(sign_data).decode())

        # sign encoded JSON to bytes
        return binance.crypto.generate_signature_for_message(
            self.wallet.private_key,
            binance.crypto.get_json_bytes_for_sign_data(sign_data)
        )

    def create_transaction(self, message, signature):
        transaction = Transaction(memo=self.memo,
                                  source=self.source,
                                  data=b'' if self.data is None else self.data)

        transaction.add_message(message)
        transaction.add_signature(Signature(public_key=self.wallet.public_key,
                                            signature=signature,
                                            account_number=self.wallet.account_number,
                                            sequence=self.wallet.sequence))

        return transaction

    def create_new_order_message(self,
                                 symbol,
                                 order_type,
                                 order_side,
                                 price,
                                 quantity,
                                 time_in_force):
        """
        Create New Order Message from parameters.

        Args:
            symbol (str): Symbol for trading pair in full name of the tokens.
            order_type (OrderType): The order type.
            order_side (OrderSide): The order side.
            price (int): Price of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer.
            quantity (int): Quantity of the order, which is the real price
                multiplied by 1e8 (10^8) and rounded to integer.
            time_in_force (TimeInForce): The time in force.

        Returns:
            NewOrderMessage: The created message object.

        """
        # get compressed address
        address = binascii.hexlify(self.wallet.address_in_bytes).decode()

        # create order ID from compressed address and sequence ID
        order_id = address.upper() + '-' + str(self.wallet.sequence + 1)

        return binance.message.NewOrderMessage(
            id=order_id,
            sender=self.wallet.address,
            symbol=symbol,
            order_type=order_type,
            order_side=order_side,
            price=price,
            quantity=quantity,
            time_in_force=time_in_force
        )

    def create_cancel_order_message(self,
                                    ref_id,
                                    symbol):
        """
        Create Cancel Order Message from parameters.

        Args:
            symbol (str): Symbol for trading pair in full name of the tokens.
            ref_id (str): The order ID of the one to cancel.

        Returns:
            CancelOrderMessage: The created message object.

        """
        return binance.message.CancelOrderMessage(
            sender=self.wallet.address,
            ref_id=ref_id,
            symbol=symbol
        )

    def create_token_freeze_message(self,
                                    symbol,
                                    amount):
        """
        Create Token Freeze from parameters.

        Args:
            symbol (str): Symbol for trading pair in full name of the tokens.
            amount (str): The amount of tokens to freeze.

        Returns:
            TokenFreezeMessage: The created message object.

        """
        return binance.message.TokenFreezeMessage(
            sender=self.wallet.address,
            amount=amount,
            symbol=symbol
        )

    def create_token_unfreeze_message(self,
                                      symbol,
                                      amount):
        """
        Create Token Unfreeze Message from parameters.

        Args:
            symbol (str): Symbol for trading pair in full name of the tokens.
            amount (str): The amount of tokens to freeze.

        Returns:
            TokenUnfreezeMessage: The created message object.

        """
        return binance.message.TokenUnfreezeMessage(
            sender=self.wallet.address,
            amount=amount,
            symbol=symbol
        )

    def create_vote_message(self,
                            proposal_id,
                            option_set):
        """
        Create Vote Message from parameters.

        Args:
            proposal_id (int): The ID of the proposal.
            option_set (VoteOption): The vote option.

        Returns:
            VoteMessage: The created message object.

        """
        return binance.message.VoteMessage(
            voter=self.wallet.address,
            proposal_id=proposal_id,
            option_set=option_set
        )

    def create_transfer_message(self,
                                coin,
                                amount,
                                recipient_address,
                                sender_address=None):
        """
        Create Transfer Message from parameters.

        Args:
            coin (str): The coin symbol (e.g. BTC, ETH, BNB, etc.).
            amount (int): The amount of tokens to transfer.
            recipient_address (str): The recipient's address.
            sender_address (str): The sender's address (defaults to wallet's
                address).

        Returns:
            TransferMessage: The created message object.

        """
        # default to wallet's address when unspecified
        if sender_address is None:
            sender_address = self.wallet.address

        return binance.message.TransferMessage(
            coin=coin,
            amount=amount,
            sender_address=sender_address,
            recipient_address=recipient_address
        )
