import datetime

def first_difference(num, num2):
    """
    >>> first_difference(2018, 2019)
    datetime.date(2019, 1, 1)
    >>> first_difference(2018, 2024)
    datetime.date(2024, 2, 29)
    >>> first_difference(2018, 2029)
    """

    a = datetime.date(num, 1, 1)
    b = datetime.date(num2, 1, 1)

    if a.weekday() != b.weekday():
        return b
    while True:
        a += datetime.timedelta(1)
        b += datetime.timedelta(1)
        if b.year != num2:
            break
        if a.day != b.day:
            return b

def reuse_calendar(num, previous=False):
    """
    >>> reuse_calendar(2018)
    2029
    >>> reuse_calendar(2018, True)
    2007
    >>> reuse_calendar(2019, previous=False)
    2030
    >>> reuse_calendar(2019, previous=True)
    2013
    """

    if previous == True:
        num2 = num - 1
        while True:
            if first_difference(num, num2) == None:
                return num2
            num2 -= 1
    if previous == False:
        num2 = num + 1
        while True:
            if first_difference(num, num2) == None:
                return num2
            num2 += 1

def reuse_calendars(num, times, previous=False):
    """
    >>> reuse_calendars(2018, 10)
    [2029, 2035, 2046, 2057, 2063, 2074, 2085, 2091, 2103, 2114]
    >>> reuse_calendars(2018, 10, True)
    [2007, 2001, 1990, 1979, 1973, 1962, 1951, 1945, 1934, 1923]
    >>> reuse_calendars(2019, 10, previous=False)
    [2030, 2041, 2047, 2058, 2069, 2075, 2086, 2097, 2109, 2115]
    >>> reuse_calendars(2019, 10, previous=True)
    [2013, 2002, 1991, 1985, 1974, 1963, 1957, 1946, 1935, 1929]
    """
    list = []
    if previous == True:
        num2 = num - 1
        while True:
            if first_difference(num, num2) == None:
                list.append(num2)
            num2 -= 1
            if len(list) == times:
                return list
    if previous == False:
        num2 = num + 1
        while True:
            if first_difference(num, num2) == None:
                list.append(num2)
            num2 += 1
            if len(list) == times:
                return list

