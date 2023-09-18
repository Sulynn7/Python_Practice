def letter_value(sentence):
    """
    >>> letter_value('OYCDHBNKEgtvuialwr')
    {'O': -9, 'Y': -8, 'C': -7, 'D': -6, 'H': -5, 'B': -4, 'N': -3, 'K': -2, 'E': -1, 'G': 1, 'T': 2, 'V': 3, 'U': 4, 'I': 5, 'A': 6, 'L': 7, 'W': 8, 'R': 9}
    >>> letter_value('abc')
    Traceback (most recent call last):
    AssertionError: invalid letters
    >>> letter_value('abba')
    Traceback (most recent call last):
    AssertionError: invalid letters
    """
    all = {}
    sentence_up = []
    for s in sentence:
        sentence_up.append(s.upper())
    c = -(int(len(sentence_up) / 2))
    if len(sentence_up) % 2 != 0:
        raise AssertionError('invalid letters')
    if len(sentence_up) != len(set(sentence_up)):
        raise AssertionError('invalid letters')
    for l in sentence_up:
        if not l.isalpha():
            raise AssertionError('invalid letters')

    for l in sentence_up:
        if c == 0:
            c += 1
        all[l] = c
        c += 1

    return all


def word_value(word, sentence):
    """
    >>> word_value('black', 'OYCDHBNKEGTVUIALWR')
    0
    >>> word_value('BROWN', 'oycdhbnkeGTVUIALWR')
    1
    >>> word_value('red', 'OYCDHBNKEgtvuialwr')
    2
    >>> word_value('SILVER', 'OYCDHBNKEGTVUIALWR')
    Traceback (most recent call last):
    AssertionError: invalid word
    """

    all = letter_value(sentence)
    c = 0
    sentence_up = []
    for l in sentence:
        sentence_up.append(l.upper())
    for l in word.upper():
        if l not in sentence_up:
            raise AssertionError('invalid word')
    for l in word.upper():
        for key, value in all.items():
            if l == key:
                c += value
    return c


def rainbow(lists, sentence):
    """
    >>> rainbow(['BLACK', 'brown', 'RED', 'orange', 'YELLOW', 'green', 'BLUE', 'violet', 'GRAY', 'White'], 'OYCDHBNKEgtvuialwr')
    True
    >>> rainbow(['BLACK', 'YELLOW', 'violet', 'green', 'White', 'orange', 'GRAY', 'BLUE', 'RED', 'brown'], 'OYCDHBNKEgtvuialwr')
    False
    >>> rainbow(('BLACK', 'brown', 'RED', 'orange', 'YELLOW', 'green', 'BLUE', 'violet', 'GRAY', 'White'), 'bwdiucankYOGTHELRV')
    False
    """

    num = []
    for l in lists:
        c = word_value(l, sentence)
        num.append(c)
    if num == sorted(num):
        if num[0] != 0:
            return False
        else:
            return True
    else:
        return False


def reflected(colors, sentence):
    """
    >>> colors = ['BLACK', 'YELLOW', 'violet', 'green', 'White', 'orange', 'GRAY', 'BLUE', 'RED', 'brown']
    >>> reflected(colors, 'OYCDHBNKEgtvuialwr')
    ('BLACK', 'brown', 'RED', 'orange', 'YELLOW', 'green', 'BLUE', 'violet', 'GRAY', 'White')
    >>> colors
    ['BLACK', 'YELLOW', 'violet', 'green', 'White', 'orange', 'GRAY', 'BLUE', 'RED', 'brown']
    >>> colors = ('BLACK', 'YELLOW', 'violet', 'green', 'White', 'orange', 'GRAY', 'BLUE', 'RED', 'brown')
    >>> reflected(colors, 'bwdiucankYOGTHELRV')
    ('BLACK', 'brown', 'BLUE', 'White', 'RED', 'GRAY', 'orange', 'YELLOW', 'green', 'violet')
    """

    num = []
    for l in colors:
        if type(l) != str:
            raise AssertionError('invalid word')
    for l in colors:
        c = word_value(l, sentence)
        num.append(c)

    dictionary = {}
    ls = []
    ll = []
    lt = []
    for l1, l2 in zip(num, colors):
        if l1 in dictionary.keys():
            ls.append(dictionary[l1])
            ls.append(l2)

            for s in ls:
                s = s.lower()
                ll.append(s)

            ll = sorted(ll)

            for t in ll:
                for k in ls:
                    if t.lower() == k.lower():
                        lt.append(k)
                        break

            dictionary[l1] = lt
        else:
            dictionary[l1] = l2


    answer = []
    for l in sorted(num):
        for key, value in dictionary.items():
            if l == key:
                if type(value) == list:
                    if value[0] not in answer:
                        answer.append(value[0])
                    if value[1] not in answer:
                        answer.append(value[1])
                else:
                    answer.append(value)
    return tuple(answer)
