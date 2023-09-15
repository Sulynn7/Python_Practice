def floors(apartments):
    """
    >>> apartments = (1, 4, 3, 2, 3, 1)
    >>> floors(apartments)
    [[False, True, False, False, False, False], [False, True, True, False, True, False], [False, True, True, True, True, False], [True, True, True, True, True, True]]
    """
    a = max(apartments)
    all_list = []
    list = []
    c = 0
    n = 1
    for i in range(a):
        c += 1
        for i, l in enumerate(apartments):
            if c == n and l >= a:
                list.append(True)
            elif c == n and l != a:
                list.append(False)
        n += 1
        a -= 1
        all_list.append(list)
        list = []

    return all_list


def front_view(apartments, width=3, distance=1, apartment='#', air=' '):
    """
    >>> apartments = (1, 4, 3, 2, 3, 1)
    >>> print(front_view(apartments, air='~'))
    ~~~~###~~~~~~~~~~~~~~~~
    ~~~~###~###~~~~~###~~~~
    ~~~~###~###~###~###~~~~
    ###~###~###~###~###~###
    >>> print(front_view(apartments, width=4, distance=0, apartment='<', air="-"))
    ----<<<<----------------
    ----<<<<<<<<----<<<<----
    ----<<<<<<<<<<<<<<<<----
    <<<<<<<<<<<<<<<<<<<<<<<<
    """
    q = []
    k = ''
    for l in floors(apartments):
        for s in l:
            if s == True:
                s = apartment * width + air * distance
            if s == False:
                s = air * width + air * distance
            k += s
        if distance == 0:
            answer = k
        else:
            answer = k[:-distance]
        q.append(answer)
        k = ''

    return '\n'.join(q)

def brush_strokes(apartments):
    """
    >>> apartments = (1, 4, 3, 2, 3, 1)
    >>> brush_strokes(apartments)
    5
    """
    all_list = floors(apartments)
    c = 0
    for l in all_list:
        for i, s in enumerate(l):
            if i < len(l) - 1:
                if l[i] == True and l[i + 1] == False:
                    c += 1
            else:
                if False not in l:
                    c += 1
                elif s == True:
                    c += 1
    return c

if __name__ == '__main__':
    import doctest
    doctest.testmod()
