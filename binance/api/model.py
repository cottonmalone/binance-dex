from collections import namedtuple
from kim import Mapper, field


class BaseModel(object):
    """
    Base model class for mapped classes.

    Provides programmatic constructor and convenience methods for equivalence
    and printing.
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.__dict__ == other.__dict__

    def __repr__(self):
        # make this look like a namedtuple
        cls = namedtuple(self.__class__.__name__, self.__dict__.keys())

        return cls(**self.__dict__).__str__()


def map_to_object(mapper_cls):
    """
    Decorator function to map the returned dictionary to mapped object.

    Args:
        mapper_cls (cls): The class of the mapper.

    Returns:
        object: The mapped object.

    """

    def wrap(f):
        def wrapped_f(*args, **kwargs):
            # create mapper with return data
            mapper = mapper_cls(data=f(*args, **kwargs))

            # return marshaled object
            return mapper.marshal()

        return wrapped_f

    return wrap


class Time(BaseModel):
    """
    Class to represent current and block time.

    Attributes:
        ap_time (datetime.datetime): Current time.
        block_time (datetime.datetime): Block time.
    """
    pass


class TimeMapper(Mapper):
    """
    Mapper for Time class.
    """
    __type__ = Time
    ap_time = field.DateTime()
    block_time = field.DateTime()
