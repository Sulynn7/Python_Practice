import datetime
from datetime import date

def birthday(date1, date2):
    """
    >>> birthday(date(1969, 10, 5), date(2015, 10, 5))
    True
    >>> birthday(date(1969, 10, 5), date(1989, 10, 4))
    False
    """

    if date1.month == date2.month:
        if date1.day == date2.day:
            return True
    return False


def sameweekday(date1, date2):
    """
    >>> sameweekday(date(1969, 10, 5), date(2002, 5, 5))
    True
    >>> sameweekday(date(1969, 10, 5), date(1989, 10, 4))
    False
    """

    if date1.day == date2.day:
        if date1.weekday() == date2.weekday():
            return True
    return False


def hundredday(date1, date2):
    """
    >>> hundredday(date(1969, 10, 5), date(1975, 10, 14))
    True
    >>> hundredday(date(1969, 10, 5), date(1989, 10, 4))
    False
    """
    diff = (date2 - date1).days
    if date1 == date2:
        return True
    if len(str(diff)) >= 3 and str(diff)[-1] == '0' and str(diff)[-2] == '0':
        return True
    else:
        return False


def unbirthday(date1, date2):
    """
    >>> unbirthday(date(1969, 10, 5), date(2015, 10, 5))
    False
    >>> unbirthday(date(1969, 10, 5), date(1989, 10, 4))
    True
    """
    if date1.month == date2.month:
        if date1.day == date2.day:
            return False
    return True


def birthdays(date1, start=datetime.date(1000, 1, 1), end=datetime.date.today(), birthday=birthday):
    """
    >>> birthdays(date(1969, 10, 5), end=date(1972, 1, 1))
    (datetime.date(1969, 10, 5), datetime.date(1970, 10, 5), datetime.date(1971, 10, 5))
    >>> birthdays(date(1969, 10, 5), birthday=sameweekday, start=date(2020, 1, 1))
    (datetime.date(2020, 1, 5), datetime.date(2020, 4, 5), datetime.date(2020, 7, 5), datetime.date(2021, 9, 5), datetime.date(2021, 12, 5), datetime.date(2022, 6, 5), datetime.date(2023, 2, 5), datetime.date(2023, 3, 5))
    >>> birthdays(date(1969, 10, 5), start=date(1975, 1, 1), end=date(1976, 1, 1), birthday=hundredday)
    (datetime.date(1975, 3, 28), datetime.date(1975, 7, 6), datetime.date(1975, 10, 14))
    """

    if start == datetime.date(1000, 1, 1):
        start = date1

    list = []

    while True:
        if birthday(date1, start) == True:
            list.append(start)
        start += datetime.timedelta(1)
        if start > end:
            break

    return tuple(list)
