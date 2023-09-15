def flip(pancakes, burnt=False):
    """
    >>> flip((9, 2, 7, 5, 8, 1, 4, 6, 3))
    (3, 6, 4, 1, 8, 5, 7, 2, 9)
    >>> flip((-9, -2, -7, 5, 8, -1, -4, -6, 3), burnt=True)
    (-3, 6, 4, 1, -8, -5, 7, 2, 9)
    """
    new_pancakes = []
    if burnt == False:
        return pancakes[::-1]
    if burnt == True:
        pancakes2 = pancakes[::-1]
        for l in pancakes2:
            if l < 0:
                new_pancakes.append(abs(l))
            if l > 0:
                new_pancakes.append(int(f'-{l}'))


        return tuple(new_pancakes)

def flip_top(pancakes, num, burnt=False):
    """
    >>> flip_top((1, 4, 6, 3, 5, 2, 7, 8, 9), 3)
    (6, 4, 1, 3, 5, 2, 7, 8, 9)
    >>> flip_top((6, 4, 1, 3, 5, 2, 7, 8, 9), 6)
    (2, 5, 3, 1, 4, 6, 7, 8, 9)
    >>> flip_top((-1, -4, -6, 3, -5, -2, 7, 8, 9), 3, burnt=True)
    (6, 4, 1, 3, -5, -2, 7, 8, 9)
    >>> flip_top((6, 4, 1, 3, -5, -2, 7, 8, 9), 1, burnt=True)
    (-6, 4, 1, 3, -5, -2, 7, 8, 9)
    >>> flip_top((-6, 4, 1, 3, -5, -2, 7, 8, 9), 6, burnt=True)
    (2, 5, -3, -1, -4, 6, 7, 8, 9)
    """

    global parts
    new_pancakes = []
    part = []
    rest = []
    for i, l in enumerate(pancakes):
        if burnt == False:
            part.append(l)
            if i + 1 == num:
                parts = part[::-1]
            elif i + 1 > num:
                rest.append(l)
                new_pancakes = parts + rest
        if burnt == True:
            rest.append(l)
            if len(rest) == num:
                rest2 = rest[::-1]
                for l in rest2:
                    if l < 0:
                        new_pancakes.append(abs(l))
                    if l > 0:
                        new_pancakes.append(int(f'-{l}'))
            elif len(rest) > num:
                new_pancakes.append(l)

    return tuple(new_pancakes)

def find_largest(pancakes, num):
    """
    >>> find_largest((1, 4, 6, 3, 5, 2, 7, 8, 9), 6)
    3
    >>> find_largest((-1, -4, -6, 3, -5, -2, 7, 8, 9), 6)
    3
    """

    part = []
    for i, l in enumerate(pancakes):
        part.append(abs(l))
        if i + 1 == num:
           large = part.index(max(part)) + 1

    return large

def sorting_step(pancakes, num, burnt=False):
    """
    >>> sorting_step((1, 4, 6, 3, 5, 2, 7, 8, 9), 6)
    (2, 5, 3, 1, 4, 6, 7, 8, 9)
    >>> sorting_step((-1, -4, -6, 3, -5, -2, 7, 8, 9), 6, burnt=True)
    (2, 5, -3, -1, -4, 6, 7, 8, 9)
    """
    a = find_largest(pancakes,num) - 1 #a까지는 그대로 num까지는 flip
    part = []
    rest = []
    for i, l in enumerate(pancakes):
        if a < i < num:
            part.append(l)
        elif i == a:
            if l >= 0:
                rest.append(l)
            elif l < 0:
                rest.append(abs(l))
        else:
            rest.append(l)
    b = flip(part, burnt)
    all = list(b) + rest
    return tuple(all)

def sorting_steps(pancakes, burnt=False):
    """
    >>> sorting_steps((1, 8, 5, 7, 2, 9, 4, 6, 3))
    [(1, 8, 5, 7, 2, 9, 4, 6, 3), (3, 6, 4, 1, 8, 5, 7, 2, 9), (2, 7, 5, 3, 6, 4, 1, 8, 9), (1, 4, 6, 3, 5, 2, 7, 8, 9), (2, 5, 3, 1, 4, 6, 7, 8, 9), (4, 1, 3, 2, 5, 6, 7, 8, 9), (2, 3, 1, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8, 9)]
    >>> sorting_steps((1, -8, -5, 7, 2, 9, -4, -6, 3), burnt=True)
    [(1, -8, -5, 7, 2, 9, -4, -6, 3), (-3, 6, 4, 1, -8, -5, 7, 2, 9), (-2, -7, 5, -3, 6, 4, 1, 8, 9), (-1, -4, -6, 3, -5, -2, 7, 8, 9), (2, 5, -3, -1, -4, 6, 7, 8, 9), (4, 1, 3, 2, 5, 6, 7, 8, 9), (-2, -3, -1, 4, 5, 6, 7, 8, 9), (1, -2, 3, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8, 9)]
    """
    all = [pancakes]
    c = 0
    while True:
        part = sorting_step(pancakes, len(pancakes) - c, burnt)
        if part == pancakes:
            pass
        else:
            all.append(tuple(part))
            pancakes = part
        c += 1
        if burnt == False:
            if list(part) == sorted(part):
                return all
        t = 0
        if burnt == True:
            for l in list(part):
                if l > 0:
                    t += 1
                    if t == len(list(part)) and list(part) == sorted(part):
                        return all
