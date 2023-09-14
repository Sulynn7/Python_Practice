def profit(list1, buy_sell):
    if type(buy_sell) == int:
        raise AssertionError('invalid actions')
    list2 = list(buy_sell)
    all_profit = 0
    alpha = ''
    not_alpha = ''
    for i in range(len(list2)):
        if i < len(list2) - 1:
            if (list2[i] == 'B' and list2[i + 1] == 'B') or (list2[i] == 'S' and list2[i + 1] == 'S'):
                raise AssertionError('invalid actions')
        if list2[i] != 'B' and list2[i] != 'S' and list2[i] != '-':
            raise AssertionError('invalid actions')
        if len(list2) != len(list1):
            raise AssertionError('invalid actions')
        if list2[i].isalpha():
            alpha += list2[i]
        if list2[i] == '-':
            not_alpha += list2[i]
    if len(not_alpha) == len(list1):
        return 0
    if alpha[0] != 'B':
        raise AssertionError('invalid actions')
    if alpha[-1] != 'S':
        raise AssertionError('invalid actions')

    for l1, l2 in zip(list1, list2):
        if l2 == 'S':
            all_profit += l1
        if l2 == 'B':
            all_profit -= l1

    return all_profit


def maximal_profit(list1):
    bit_coins = 'x'
    all_profit = 0
    for i in range(len(list1)):
        if i < len(list1) - 1:
            if bit_coins == 'x':
                if list1[i] < list1[i + 1]:
                    all_profit -= list1[i]
                    bit_coins = 'o'
            elif bit_coins == 'o':
                if list1[i] > list1[i + 1]:
                    all_profit += list1[i]
                    bit_coins = 'x'
        if i + 1 == len(list1):
            if bit_coins == 'o':
                all_profit += list1[-1]

    return all_profit

def optimal_actions(list1):
    bit_coins = 'x'
    all_profit = ''
    for i in range(len(list1)):
        if i < len(list1) - 1:
            if bit_coins == 'x':
                if list1[i] < list1[i + 1]:
                    all_profit += 'B'
                    bit_coins = 'o'
                else:
                    all_profit += '-'
            elif bit_coins == 'o':
                if list1[i] > list1[i + 1]:
                    all_profit += 'S'
                    bit_coins = 'x'
                else:
                    all_profit += '-'
        if i + 1 == len(list1):
            if bit_coins == 'o':
                all_profit += 'S'
            else:
                all_profit += '-'

    return all_profit