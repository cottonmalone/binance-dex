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
