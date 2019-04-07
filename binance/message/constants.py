from enum import Enum


class OrderSide(Enum):
    BUY = 1
    SELL = 2


class OrderType(Enum):
    LIMIT = 2


class TimeInForce(Enum):
    GTE = 1
    """
    Good Till Expire
    """
    IOC = 3
    """
    Immediate Or Cancel
    """
