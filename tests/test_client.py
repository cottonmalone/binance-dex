from binance import *
import binance.api


def get_test_client():
    return Client(BinanceNetwork.TEST)


def test_client_get_time(mocker):
    """
    Test that methods behaves as expected.
    """
    # get client
    client = get_test_client()

    # check return type is as expected
    assert isinstance(client.get_time(), binance.api.Time)
