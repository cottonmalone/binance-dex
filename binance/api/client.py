from .operations import get, post


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
