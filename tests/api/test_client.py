from binance.api import *


def test_client_ctor():
    """
    Test that object is initialised correctly.
    """
    assert Client('url').base_url == 'url'


def test_client_get_time(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_time() == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/time')


def test_client_get_node_info(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_node_info() == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/node-info')


def test_client_get_validators(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_node_info() == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/validators')


def test_client_get_peers(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_node_info() == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/peers')
