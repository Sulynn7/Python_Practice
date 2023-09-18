def list_representation(number, n):
    """
    >>> grid = list_representation('1221133113322222', 4)
    >>> grid
    [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
    """
    grid = []
    inner = []
    for l in number:
        inner.append(int(l))
        if len(inner) == n:
            grid.append(inner)
            inner = []
    return grid

def string_representation(grid):
    """
    >>> grid = list_representation('1221133113322222', 4)
    >>> string_representation(grid)
    ('1221133113322222', 4, 4)
    """
    answer = []
    string_version = ''
    for l in grid:
        for l2 in l:
            string_version += str(l2)

    answer.append(string_version)
    answer.append(len(grid))
    answer.append(len(grid[0]))

    return tuple(answer)

def move(how_much, which_part, grid):
    """
    >>> grid = list_representation('1221133113322222', 4)
    >>> grid
    [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
    >>> move(-1, {(1, 2), (1, 1), (2, 1), (2, 2)}, grid)
    [[1, 2, 2, 1], [1, 2, 2, 1], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> grid
    [[1, 2, 2, 1], [1, 2, 2, 1], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> move(+1, {(0, 3), (1, 3)}, grid)
    [[1, 2, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> grid
    [[1, 2, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> move(+1, {(2, 0), (1, 0), (0, 0)}, grid)
    [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
    """

    which_part2 = list(which_part)
    for l in which_part2:
        original = grid[l[0]][l[-1]]
        new = original + how_much
        grid[l[0]][l[1]] = new

    return grid

def is_solved(grid):
    """
    >>> grid = list_representation('1221133113322222', 4)
    >>> grid
    [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
    >>> move(-1, {(1, 2), (1, 1), (2, 1), (2, 2)}, grid)
    [[1, 2, 2, 1], [1, 2, 2, 1], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> grid
    [[1, 2, 2, 1], [1, 2, 2, 1], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> move(+1, {(0, 3), (1, 3)}, grid)
    [[1, 2, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> grid
    [[1, 2, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> move(+1, {(2, 0), (1, 0), (0, 0)}, grid)
    [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
    >>> grid
    [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
    >>> is_solved(grid)
    True
    """
    all = []
    for l in grid:
        for l2 in l:
            all.append(l2)

    if len(set(all)) == 1:
        return True
    else:
        return False

def group(which_part, grid):
    """
    >>> grid = list_representation('1221133113322222', 4)
    >>> grid
    [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
    >>> group((2, 1), grid)
    {(1, 2), (1, 1), (2, 1), (2, 2)}
    >>> group((0, 3), grid)
    {(0, 3), (1, 3)}
    >>> group((1, 0), grid)
    {(2, 0), (1, 0), (0, 0)}
    """
    specific = grid[which_part[0]][which_part[1]]

    coor = []
    final = []
    for i, l in enumerate(grid):
        for i2, l2 in enumerate(l):
            if l2 == specific:
                coor.append(i)
                coor.append(i2)
                if i == which_part[0]:
                    if abs(which_part[1] - i2) > 1:
                        coor = []
                    else:
                        final.append(tuple(coor))
                        coor = []
                elif i2 == which_part[1]:
                    if abs(which_part[0] - i) > 1:
                        coor = []
                    else:
                        final.append(tuple(coor))
                        coor = []
                else:
                    if len(final) > 0:
                        for s in final: # final =[(0,3)]
                            if i == s[0]:
                                if abs(s[1] - i2) > 1:
                                    coor = []
                                else:
                                    final.append(tuple(coor))
                                    break
                            elif i2 == s[1]:
                                if abs(s[0] - i) > 1:
                                    coor = []
                                else:
                                    final.append(tuple(coor))
                                    break
                            else:
                                pass
                    coor = []

    return set(final)


def is_solution(moving, grid):
    """
    >>> grid = [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
    >>> is_solution([(1, 1, False), (3, 2, False)], grid)
    True
    """
    for i, l in enumerate(moving):
        if i == 0:
            grouping = group(l[:2], grid)
            if l[-1] == True:
                grid = move(+1, grouping, grid)
            else:
                grid = move(-1, grouping, grid)
        else:
            specific = grid[l[0]][l[1]]

            coor = []
            final = []
            for i, l in enumerate(grid):
                for i2, l2 in enumerate(l):
                    if l2 == specific:
                        coor.append(i)
                        coor.append(i2)
                        final.append(tuple(coor))
                        coor = []
            grouping = set(final)
            if l[-1] == True:
                grid = move(+1, grouping, grid)
            else:
                grid = move(-1, grouping, grid)
    return is_solved(grid)
