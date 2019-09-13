import DayOfWeekBL
from datetime import date, datetime

today = date.today()


def test_day():
    day = int(today.strftime("%d"))
    month = int(today.strftime("%m"))
    year = int(today.strftime("%Y"))
    assert str(today.strftime("%A")) == DayOfWeekBL.dayOfWeek(year, month, day)


def test_day1():
    day = 13
    month = 9
    year = 2019
    assert 'Friday' == DayOfWeekBL.dayOfWeek(year, month, day)
