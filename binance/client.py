import binance.api


class Client(object):

    def __init__(self, network):
        self.network = network.value

        self.api = binance.api.Client(self.network.api_url)

    @binance.api.map_to_object(binance.api.TimeMapper)
    def get_time(self):
        """
        Gets the latest block time and the current time according to the HTTP
        service.

        Returns:
            binance.api.Time: The response data.

        Raises:
            BadRequest: If the input is malformed.
            NotFound: If the resource could not be found.
            UnknownError: For any unexpected error.

        """
        return self.api.get_time()
