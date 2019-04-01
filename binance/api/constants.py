from enum import Enum


class Interval(Enum):
    # minutes
    INT_1_MINUTE = "1m"
    INT_3_MINUTES = "3m"
    INT_5_MINUTES = "5m"
    INT_15_MINUTES = "15m"
    INT_30_MINUTES = "30m"

    # hours
    INT_1_HOUR = "1h"
    INT_2_HOURS = "2h"
    INT_4_HOURS = "4h"
    INT_6_HOURS = "6h"
    INT_8_HOURS = "8h"
    INT_12_HOURS = "12h"

    # days
    INT_1_DAY = "1d"
    INT_3_DAYS = "3d"
    INT_1_WEEK = "1w"
    INT_1_MONTH = "1M"
