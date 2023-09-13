def evenOdd(number):
    """
    >>> evenOdd(886328712442992)
    (10, 5)
    >>> evenOdd(10515)
    (1, 4)
    >>> evenOdd(145)
    (1, 2)
    """
    even = ''
    odd = ''
    for n in str(number):
        if int(n) % 2 == 0:
            even += n
        else:
            odd += n

    return (len(even), len(odd))

def step(number):
    """
    >>> step(886328712442992)
    10515
    >>> step(10515)
    145
    >>> step(145)
    123
    """
    even = ''
    odd = ''
    for n in str(number):
        if int(n) % 2 == 0:
            even += n
        else:
            odd += n
    a = str(len(even)) + str(len(odd)) + str(len(str(number)))
    return int(a)

def steps(number):

    """
    >>> steps(886328712442992)
    3
    >>> steps(1217637626188463187643618416764317864)
    4
    >>> steps(0)
    2
    >>> steps(1)
    5
    >>> steps(2)
    2
    >>> steps(3)
    5
    """
    if number == 123:
        return 0
    c = 0
    while True:
        even = ''
        odd = ''
        for n in str(number):
            if int(n) % 2 == 0:
                even += n
            else:
                odd += n
        number = str(len(even)) + str(len(odd)) + str(len(str(number)))
        if '0' in number[0]:
            number = number[1:]
        c += 1
        if number == '123':
            return c


if __name__ == '__main__':
    import doctest
    doctest.testmod()
