def positions(letter):
    """
    >>> positions('LOVE')
    (11, 14, 21, 4)
    >>> positions('mutual')
    (12, 20, 19, 20, 0, 11)
    """
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    num = []
    for i, l in enumerate(letter):
        if l in ALPHABET:
            num.append(ALPHABET.index(l))
        if l in alphabet:
            num.append(alphabet.index(l))
    num = tuple(num)
    return num



def ismutual(list, number):
    """
    >>> ismutual((11, 14, 21, 4), 26)
    True
    >>> ismutual([12, 20, 19, 20, 0, 11], 26)
    False
    """
    number2 = number - 1
    c = 0
    for l in list:
        if abs(number2 - int(l)) in list:
            c += 1
            if c == len(list):
                return True
        else:
            return False

def mutual_love(letter):
    """
    >>> mutual_love('LOVE')
    True
    >>> mutual_love('mutual')
    False
    """
    num = positions(letter)
    answer = ismutual(num, 26)
    if answer == True:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
