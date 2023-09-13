def longestPolydivisiblePrefix(number):
    """
    >>> longestPolydivisiblePrefix(1234356789)
    123
    >>> longestPolydivisiblePrefix(381654729)
    381654729
    >>> longestPolydivisiblePrefix(381654728)
    38165472
    """
    c = 0
    prefix = ''
    for n in str(number):
        c += 1
        prefix += n
        if int(prefix) % c != 0:
            return int(prefix[:-1])

    if int(number) % len(str(number)) == 0:
        return int(number)

def isPolydivisible(number):
    """
    >>> isPolydivisible(1234356789)
    False
    >>> isPolydivisible(381654729)
    True
    >>> isPolydivisible(381654728)
    False
    """
    if longestPolydivisiblePrefix(number) == int(number):
        return True
    else:
        return False

def polydivisibleExtensions(number):
    """
    >>> polydivisibleExtensions(12)
    4
    >>> polydivisibleExtensions(23)
    0
    >>> polydivisibleExtensions(381654729)
    1
    """
    if isPolydivisible(number) == False:
        return 0
    else:
        c = 0
        s = 0
        for n in range(10):

            number2 = str(str(number) + str(c))
            if int(number2) % len(str(number2)) == 0:
                s += 1
            c += 1

        return s

if __name__ == '__main__':
    import doctest
    doctest.testmod()