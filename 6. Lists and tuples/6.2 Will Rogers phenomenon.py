def average(list):
    """
    >>> average((5, 6, 7, 8, 9))
    7.0
    >>> average([1, 2, 3, 4])
    2.5
    """
    sum = 0
    for l in list:
        sum += int(l)

    return sum/len(list)

def move1(seq1, seq2, seq3):
    """
    >>> seq1 = [5, 6, 7, 8, 9]
    >>> seq2 = [1, 2, 3, 4]
    >>> seq3 = [5]
    >>> move1(seq1, seq2, seq3)
    >>> seq1
    [6, 7, 8, 9]
    >>> seq2
    [1, 2, 3, 4, 5]
    >>> seq3
    [5]
    """
    for i in seq3:
        seq2.append(i)

    for i in range(len(seq1)):
        for s in seq1:
            if s in seq3:
                seq1.remove(s)
                seq3 = list(seq3)
                seq3.remove(s)

def move2(seq1, seq2, seq3):
    """
    >>> seq1 = (5, 6, 7, 8, 9)
    >>> seq2 = [1, 2, 3, 4]
    >>> seq3 = [5]
    >>> move2(seq1, seq2, seq3)
    ([6, 7, 8, 9], [1, 2, 3, 4, 5])
    >>> seq1
    (5, 6, 7, 8, 9)
    >>> seq2
    [1, 2, 3, 4]
    >>> seq3
    [5]
    """
    seq22 = []

    seq1 = list(seq1)
    seq2 = list(seq2)
    seq3 = list(seq3)

    for i in seq2:
        seq22.append(i)
    for i in seq3:
        seq22.append(i)

    for s in seq1:
        if s in seq3:
            seq1.remove(s)
            seq3.remove(s)
    return seq1, seq22

def iswillrogers(seq1, seq2, seq3):
    """
    >>> iswillrogers([5, 6, 7, 8, 9], [1, 2, 3, 4], [5])
    True
    >>> iswillrogers((5, 6, 7, 8, 9), (1, 2, 3, 4), (7, 9))
    False
    """
    seq1_a = average(seq1)
    seq2_a = average(seq2)

    seq11, seq22 = move2(seq1, seq2, seq3)
    seq11_a = average(seq11)
    seq22_a = average(seq22)
    if seq1_a < seq11_a and seq2_a < seq22_a:
        return True
    else:
        return False



if __name__ == '__main__':
    import doctest
    doctest.testmod()



