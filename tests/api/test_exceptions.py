import pytest
from binance.api.exceptions import *


@pytest.mark.parametrize('code,expected_exception', [
    (400, BadRequest),
    (404, NotFound),
    (10000, UnknownError)
])
def test_generate_exception_for_code(code, expected_exception):
    """
    Test function behaves as expected
    """
    result = generate_exception_for_code(code, 'foo')

    # check result is as expected
    assert isinstance(result, expected_exception)
    assert str(result) == 'foo'
