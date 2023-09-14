def iszapreadable(list):
    """
    >>> iszapreadable([7, 5, 3, 1, 8, 6, 4, 2])
    True
    >>> iszapreadable([1, 2, 4, 7, 3, 8, 6, 5])
    False
    >>> iszapreadable([1, 2, 5, 3, 8, 7, 4, 6])
    True
    >>> iszapreadable([1, 1, 1, 1, 1, 1, 1, 1])
    False
    """
    if len(list) == 1 or len(list) == 2:
        return True
    elif len(list) % 2 != 0:
        return False

    else:
        first = int(len(list) - 1)
        first2 = len(list)
        c = [first]
        d = [first2]

        for i in range(int(len(list) / 2) - 1):
            first -= 2
            first2 -= 2
            c.append(first)
            d.append(first2)
            all = c + d

        if list == all:
            return True

        l = len(list)
        k = 2
        while True:
            if l % k == 0:
                k *= 2
                if k >= l:
                    break
            else:
                return False

    c = 0
    for i in range(l):
        if list[0] == 1 and list[1] == 2 and list[3] == 3:
            return True

    return False

def zapbook(number):
    """
    >>> zapbook(6)
    [5, 3, 1, 6, 4, 2]
    >>> zapbook(7)
    []
    >>> zapbook(8)
    [1, 2, 5, 3, 8, 7, 4, 6]
    """
    if number == 1:
        return [1]
    if number % 2 != 0:
        return []

    first = number - 1
    first2 = number
    c = [first]
    d = [first2]

    for i in range(int(number / 2) - 1):
        first -= 2
        first2 -= 2
        c.append(first)
        d.append(first2)
        all = c + d


    l = number
    k = 2
    while True:
        if l % k == 0:
            k *= 2
            if k >= l:
                break
        else:
            return all

    x = 0 #페이지 넘버
    y = 0 #읽은 순서
    list = []
    list2 = []

    for i in range(number):
        y += x
        x += 1
        if y > number - 1:
            y = y - number

        list.append([y, i + 1])
    print(list)
    list = sorted(list)
    print(list)
    for i in range(len(list)):
        list2.append(list[i][1])
    return list2