import pytest
import datetime
from binance.api import *

POSIX_ORGIN = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)


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
    assert Client('url').get_validators() == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/validators')


def test_client_get_peers(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_peers() == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/peers')


def test_client_get_account(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_account('id') == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/account/id')


def test_client_get_account_sequence(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_account_sequence('id') == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/account/id/sequence')


def test_client_get_transaction(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_transaction('id') == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/tx/id?format=json')


def test_client_get_tokens(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_tokens('offset', 'limit') == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/tokens', params={
        'offset': 'offset',
        'limit': 'limit'
    })


def test_client_get_markets(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_markets('offset', 'limit') == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/markets', params={
        'offset': 'offset',
        'limit': 'limit'
    })


def test_client_get_fees(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_fees() == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/fees')


def test_client_get_depth(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_depth('symbol', 'limit') == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/depth', params={
        'symbol': 'symbol',
        'limit': 'limit'
    })


def test_client_broadcast(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    post = mocker.patch('binance.api.client.post', return_value='foo')

    # check that return value is correct
    assert Client('url').broadcast('transaction', 'sync') == 'foo'

    # check that mock functions were called as expected
    post.assert_called_with('url',
                            '/api/v1/broadcast',
                            headers={"Content-Type": "text/plain"},
                            params={'sync': 'sync'},
                            data='transaction')


@pytest.mark.parametrize('start_time,end_time,exp_start_time,exp_end_time', [
    (None, None, None, None),
    (POSIX_ORGIN, POSIX_ORGIN, 0, 0)
])
def test_client_get_klines(start_time,
                           end_time,
                           exp_start_time,
                           exp_end_time,
                           mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_klines('symbol',
                                    Interval.INT_1_DAY,
                                    'limit',
                                    start_time,
                                    end_time) == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/klines', params={
        'symbol': 'symbol',
        'interval': '1d',
        'limit': 'limit',
        'startTime': exp_start_time,
        'endTime': exp_end_time,
    })


@pytest.mark.parametrize('start_time,end_time,exp_start_time,exp_end_time', [
    (None, None, None, None),
    (POSIX_ORGIN, POSIX_ORGIN, 0, 0)
])
def test_client_get_closed_orders(start_time,
                                  end_time,
                                  exp_start_time,
                                  exp_end_time,
                                  mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_closed_orders('address',
                                           'symbol',
                                           OrderStatus.ACK,
                                           Side.BUY,
                                           'offset',
                                           'limit',
                                           True,
                                           start_time,
                                           end_time) == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/orders/closed', params={
        'address': 'address',
        'symbol': 'symbol',
        'status': 'Ack',
        'side': 1,
        'offset': 'offset',
        'limit': 'limit',
        'total': 1,
        'start': exp_start_time,
        'end': exp_end_time,
    })


def test_client_get_open_orders(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_open_orders('address',
                                         'symbol',
                                         'offset',
                                         'limit',
                                         True) == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/orders/open', params={
        'address': 'address',
        'symbol': 'symbol',
        'offset': 'offset',
        'limit': 'limit',
        'total': 1
    })


def test_client_get_order(mocker):
    """
    Test that methods behaves as expected.
    """
    # mock all underlying functionality
    get = mocker.patch('binance.api.client.get', return_value='foo')

    # check that return value is correct
    assert Client('url').get_order('id') == 'foo'

    # check that mock functions were called as expected
    get.assert_called_with('url', '/api/v1/orders/id')
