import requests
import urllib3
import pytest
from binance.api.operations import *


def test_perform_request_success(mocker):
    """
    Test function behaves as expected when request is successful.
    """
    # mock all underlying functionality
    response = mocker.MagicMock()
    response.status_code = 200
    response.json.return_value = 'json_data'

    request_fct = mocker.MagicMock()
    request_fct.return_value = response

    # check that return value is correct
    assert perform_request(request_fct,
                           'foo',
                           '/bar',
                           'arg',
                           karg='karg') == 'json_data'

    # check that mock functions were called as expected
    request_fct.assert_called_with(urllib3.util.Url(host='foo',
                                                    path='/bar'),
                                   'arg',
                                   karg='karg')


def test_perform_request_error(mocker):
    """
    Test function behaves as expected when request returns an error code.
    """
    # mock all underlying functionality
    response = mocker.MagicMock()
    response.status_code = 400
    response.json.return_value = {'message': 'foo'}

    request_fct = mocker.MagicMock()
    request_fct.return_value = response

    generate_exception_for_code = \
        mocker.patch('binance.api.operations.generate_exception_for_code',
                     return_value=RuntimeError())

    # check that return value is correct
    with pytest.raises(RuntimeError):
        assert perform_request(request_fct,
                               'foo',
                               '/bar',
                               'arg',
                               karg='karg') == 'json_data'

    # check that mock functions were called as expected
    request_fct.assert_called_with(urllib3.util.Url(host='foo',
                                                    path='/bar'),
                                   'arg',
                                   karg='karg')
    generate_exception_for_code.assert_called_with(400, 'foo')


def test_get(mocker):
    """
    Test function behaves as expected.
    """
    # mock all underlying functionality
    perform_request = mocker.patch('binance.api.operations.perform_request',
                                   return_value='foo')

    # check that return value is correct
    assert get('foo',
               '/bar',
               'arg',
               karg='karg') == 'foo'

    # check that mock functions were called as expected
    perform_request.assert_called_with(requests.get,
                                       'foo',
                                       '/bar',
                                       'arg',
                                       karg='karg')


def test_post(mocker):
    """
    Test function behaves as expected.
    """
    # mock all underlying functionality
    perform_request = mocker.patch('binance.api.operations.perform_request',
                                   return_value='foo')

    # check that return value is correct
    assert post('foo',
                '/bar',
                'arg',
                karg='karg') == 'foo'

    # check that mock functions were called as expected
    perform_request.assert_called_with(requests.post,
                                       'foo',
                                       '/bar',
                                       'arg',
                                       karg='karg')
