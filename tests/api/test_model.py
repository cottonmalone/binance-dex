from binance import *
from binance.api import *
from datetime import datetime


def test_base_model():
    """
    Test that base model objects behaves as expected.
    """
    # use programmatic constructor
    base = BaseModel(foo='foo',
                     bar='bar')

    # check that constructor assigns the fields
    assert base.__dict__ == {"bar": "bar", "foo": "foo"}

    # check that equivalence checks contents
    assert base == BaseModel(foo='foo',
                             bar='bar')

    # check that it prints the object in JSON format
    assert str(base) == "BaseModel(foo='foo', bar='bar')"


def test_map_to_object_decorator(mocker):
    """
    Test that decorator behaves as expected.
    """

    # mock object class
    class MockObj(BaseModel):
        pass

    # mock mapper class
    class MockMapper(Mapper):
        __type__ = MockObj
        foo = field.String()

    # create mock function to be decorated
    mock_fct = mocker.MagicMock()
    mock_fct.return_value = {'foo': 'bar'}

    # apply decorator
    fct = map_to_object(MockMapper)(mock_fct)

    # check that result matches expected
    assert fct('foo', bar='bar') == MockObj(foo="bar")

    # check that decorated function was called with the right arguments
    mock_fct.assert_called_with('foo', bar='bar')


def test_time_mapper():
    """
    Test that mapper works with API response sample.
    """
    # sample from actual API
    response = {
        'ap_time': '2019-04-07T18:28:43Z',
        'block_time': '2019-04-07T18:28:42Z'
    }

    # check that object is parsed correctly
    assert TimeMapper(data=response).marshal() == \
           Time(ap_time=datetime.fromisoformat('2019-04-07 18:28:43+00:00'),
                block_time=datetime.fromisoformat('2019-04-07 18:28:42+00:00'))
