def numbers(lists):
    """
    >>> numbers([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    >>> numbers([[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
    >>> numbers([[2, 15, 5, 13], [16, 3, 7, 12], [9, 8, 14, 1], [6, 4, 11, 10]])
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
    """
    full = []
    for l in lists:
        for s in l:
            full.append(s)

    return set(sorted(full))

def sums(lists):
    """
    >>> sums([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    {15}
    >>> sums([[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    {34, 35, 36, 40, 10, 42, 26, 58, 29, 31}
    >>> sums([[2, 15, 5, 13], [16, 3, 7, 12], [9, 8, 14, 1], [6, 4, 11, 10]])
    {32, 33, 34, 35, 36, 37, 38, 29, 30, 31}
    """
    full = []
    plus = []
    c = 0
    for i in range(len(lists)):
        plus.append(lists[i][i])
    full.append(sum(plus))
    plus = []
    for i in range(len(lists)):
        plus.append(lists[i][-(i + 1)])
    full.append(sum(plus))
    plus = []
    for i in range(len(lists)):
        for i in range(len(lists)):
            plus.append(lists[i][c])
        full.append(sum(plus))
        plus = []
        c += 1
    for l in lists:
        plus = sum(l)
        full.append(plus)

    return set(full)

def ismagic(lists):
    """
    >>> ismagic([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    True
    >>> ismagic([[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    False
    >>> ismagic([[2, 15, 5, 13], [16, 3, 7, 12], [9, 8, 14, 1], [6, 4, 11, 10]])
    False
    """
    full = []
    sets = sums(lists)
    if len(sets) == 1:
        for l in lists:
            for s in l:
                full.append(s)
        set2 = set(full)
        if len(full) != len(set2):
            return False
        else:
            return True
    else:
        return False

def ishetero(lists):
    """
    >>> ishetero([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    False
    >>> ishetero([[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    True
    >>> ishetero([[2, 15, 5, 13], [16, 3, 7, 12], [9, 8, 14, 1], [6, 4, 11, 10]])
    True
    """

    sets = sums(lists)
    full = []
    if len(sets) == len(lists) * 2 + 2:
        for l in lists:
            for s in l:
                full.append(s)
        set2 = set(full)
        if len(full) != len(set2):
            return False
        else:
            return True
    else:
        return False

def isantimagic(lists):
    """
    >>> isantimagic([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    False
    >>> isantimagic([[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    False
    >>> isantimagic([[2, 15, 5, 13], [16, 3, 7, 12], [9, 8, 14, 1], [6, 4, 11, 10]])
    True
    """

    sets = sums(lists)
    list_a = list(sets)
    big = max(list_a)
    small = min(list_a)
    answer = ishetero(lists)
    if answer == True:
        if (big + small) * (len(list_a) / 2) == sum(list_a):
            return True
        else:
            return False
    else:
        return False
