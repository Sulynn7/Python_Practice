def group(cards, number):
    all = []
    list = []
    if type(number) == int:
        if len(cards) % number != 0:
            raise AssertionError('invalid grouping')
        for i, l in enumerate(cards):
            i += 1
            if i % number != 0:
                list.append(l)
            if i % number == 0:
                list.append(l)
                all.append(tuple(list))
                list = []
    else:
        n = 0
        for s in number:
            if type(s) == str:
                raise AssertionError('invalid grouping')
            elif s <= 0:
                raise AssertionError('invalid grouping')
            n += int(s)
        if len(cards) != n:
            raise AssertionError('invalid grouping')
        for i, l in enumerate(number):
            if i == 0:
                a = int(l)
                list = cards[:a]
                all.append(tuple(list))
            else:
                list = cards[a:a + l]
                all.append(tuple(list))
                a = a + l

    return all

def riffle_shuffle(pile1, pile2):
    list = []
    if len(pile1) != len(pile2):
        raise AssertionError('different number of groups')
    for l1, l2 in zip(pile1, pile2):
        for s in l1:
            list.append(s)
        for s in l2:
            list.append(s)

    return list

def mixed_pairs(new_pile):
    if len(new_pile) % 2 != 0:
        raise AssertionError('odd number of cards')
    all = group(new_pile, 2)
    c = 0
    red = []
    black = []
    if type(all) == list:
        for l in all:
            if l[0][-1] == 'C' or l[0][-1] == 'S':
                black.append(l[0])
            if l[0][-1] == 'D' or l[0][-1] == 'H':
                red.append(l[0])
            if l[1][-1] == 'C' or l[1][-1] == 'S':
                black.append(l[1])
            if l[1][-1] == 'D' or l[1][-1] == 'H':
                red.append(l[1])
            c += 1
            k = 0
            if c == len(all) - 1:
                for l in all:

                    if (l[0] in black and l[1] in red) or (l[0] in red and l[1] in black):
                        k += 1
                        if k == len(all) - 1:
                            return True
                    else:
                        return False
