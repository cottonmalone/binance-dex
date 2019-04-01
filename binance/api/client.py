from .operations import get, post
from .constants import *


class Client(object):
    """
    Class for Binance API client.
    """

    def __init__(self, base_url):
        """
        Args:
            base_url (str): The host URL for the Binance DEX API.
        """
        self.base_url = base_url

    def get_time(self):
        """
        Gets the latest block time and the current time according to the HTTP
        service.

        Returns:
            dict: The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/time')

    def get_node_info(self):
        """
        Gets runtime information about the node.

        Returns:
            dict: The response data.

        """
        return get(self.base_url, '/api/v1/node-info')

    def get_validators(self):
        """
        Gets the list of validators used in consensus.

        Returns:
            list(dict): The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/validators')

    def get_peers(self):
        """
        Gets the list of network peers.

        Returns:
            list(dict): The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/peers')

    def get_account(self, address):
        """
        Gets account metadata for an address.

        Args:
            address (str): The account's address.

        Returns:
            dict: The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/account/{}'.format(address))

    def get_account_sequence(self, address):
        """
        Gets an account sequence for an address.

        Args:
            address (str): The account's address.

        Returns:
            dict: The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/account/{}/sequence'.format(address))

    def get_transaction(self, hash):
        """
        Gets transaction metadata by transaction ID.

        Args:
            hash (str): The transaction's ID.

        Returns:
            dict: The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/tx/{}?format=json'.format(hash))

    def get_tokens(self, offset=0, limit=500):
        """
        Gets a list of tokens that have been issued.

        Args:
            offset (int): The offset for the query.
            limit (int): The limit for the query.

        Returns:
            list(dict): The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/tokens', params={
            'offset': offset,
            'limit': limit
        })

    def get_markets(self, offset=0, limit=500):
        """
        Gets the list of market pairs that have been listed.

        Args:
            offset (int): The offset for the query.
            limit (int): The limit for the query.

        Returns:
            list(dict): The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/markets', params={
            'offset': offset,
            'limit': limit
        })

    def get_fees(self):
        """
        Gets the current trading fees settings.

        Returns:
            list(dict): The response data.

        Raises:
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/fees')

    def get_depth(self, symbol, limit=500):
        """
        Gets the order book depth data for a given pair symbol.

        Args:
            symbol (str): Market pair symbol, e.g. NNB-0AD_BNB.
            limit (int): The limit of results.
                Allowed limits: [5, 10, 20, 50, 100, 500, 1000]

        Returns:
            list(dict): The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/depth', params={
            'symbol': symbol,
            'limit': limit
        })

    def broadcast(self, transaction, sync=False):
        """
        Broadcasts a signed transaction.

        A single transaction must be sent hex-encoded in byte form.

        Args:
            transaction (bytes): Raw content of transaction in hex-encoded form.
            sync (bool): Whether the function should wait for DeliverTx
                confirmation.

        Returns:
            list(dict): The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return post(self.base_url,
                    '/api/v1/broadcast',
                    headers={"Content-Type": "text/plain"},
                    params={'sync': sync},
                    data=transaction)

    def get_klines(self,
                   symbol,
                   interval,
                   limit=500,
                   start_time=None,
                   end_time=None):
        """
        Gets candlestick/kline bars for a symbol.

        Bars are uniquely identified by their open time.

        If the time window is larger than limits, only the first n klines
        will return. In this case, please either shrink the window or
        increase the limit to get proper amount of klines.

        Args:
            symbol (str): Market pair symbol, e.g. NNB-0AD_BNB.
            interval (Interval). The interval for the chart.
            limit (int): The limit of results.
                Allowed limits: [5, 10, 20, 50, 100, 500, 1000]
            start_time (datetime): The start time for the interval.
            end_time (datetime): The end time for the interval.

        Returns:
            list(dict): The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/klines', params={
            'symbol': symbol,
            'interval': interval.value,
            'limit': limit,
            # convert datetime to POSIX timestamp in milliseconds
            'startTime': start_time.timestamp() * 1000 if start_time else None,
            'endTime': end_time.timestamp() * 1000 if end_time else None
        })

    def get_closed_orders(self,
                          address,
                          symbol=None,
                          status=OrderStatus.ALL,
                          side=Side.BOTH,
                          offset=0,
                          limit=500,
                          total=False,
                          start_time=None,
                          end_time=None):
        """
        Gets closed (filled and cancelled) orders for a given address.

        Warnings:
            Default query window is latest 7 days.
            The maximum start - end query window is 3 months.

        Args:
            address (str): The owner's address.
            symbol (str): Market pair symbol, e.g. NNB-0AD_BNB.
            status (OrderStatus). The status of the order.
            side (Side): The order's side.
            offset (int): The offset for the query.
            limit (int): The limit of results.
                Allowed limits: [5, 10, 20, 50, 100, 500, 1000]
            total (bool): Whether to include the total number of returned
                orders in the response. If set to False, the total will be
                set to -1 in the response.
            start_time (datetime): The start time for the interval.
            end_time (datetime): The end time for the interval.

        Returns:
            list(dict): The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/orders/closed', params={
            'address': address,
            'symbol': symbol,
            'status': status.value,
            'side': side.value,
            'offset': offset,
            'limit': limit,
            'total': int(total),
            # convert datetime to POSIX timestamp in milliseconds
            'start': start_time.timestamp() * 1000 if start_time else None,
            'end': end_time.timestamp() * 1000 if end_time else None
        })

    def get_open_orders(self,
                        address,
                        symbol=None,
                        offset=0,
                        limit=500,
                        total=False):
        """
        Gets open orders for a given address.

        Args:
            address (str): The owner's address.
            symbol (str): Market pair symbol, e.g. NNB-0AD_BNB.
            offset (int): The offset for the query.
            limit (int): The limit of results.
                Allowed limits: [5, 10, 20, 50, 100, 500, 1000]
            total (bool): Whether to include the total number of returned
                orders in the response. If set to False, the total will be
                set to -1 in the response.

        Returns:
            list(dict): The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/orders/open', params={
            'address': address,
            'symbol': symbol,
            'offset': offset,
            'limit': limit,
            'total': int(total)
        })

    def get_order(self, id):
        """
        Gets metadata for an individual order by its ID.

        Args:
            id (str): The order's ID.

        Returns:
            dict: The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return get(self.base_url, '/api/v1/orders/{}'.format(id))
