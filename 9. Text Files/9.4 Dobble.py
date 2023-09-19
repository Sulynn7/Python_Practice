def card2symbols(words):
    """
    >>> c2s = card2symbols('cards.txt')
    >>> c2s[1]
    {'cheese', 'eye', 'heart', 'ice cube', 'light bulb', 'snowman', 'water drip'}
    >>> c2s[2]
    {'exclamation point', 'eye', 'ice cube', 'red lips', 'scissors', 'snowman', 'treble clef', 'zebra'}
    >>> c2s[3]
    {'daisy flower', 'ice cube', 'light bulb', 'red lips', 'snowman', 'treble clef', 'zebra'}
    """
    value_list = []
    c2s = {}
    for i, line in enumerate(open(words, 'r')):
        for word in line:
            if ',' in line:
                a = line[:line.index(',')]
                value_list.append(a)
                line = line[line.index(',') + 1:]
            else:
                value_list.append(line.rstrip('\n'))
        c2s[i + 1] = set(value_list)
        value_list = []

    return c2s

def common_symbols(card1, card2, c2s):
    """
    >>> c2s = card2symbols('cards.txt')
    >>> common_symbols(1, 2, c2s)
    {'eye', 'ice cube', 'snowman'}
    >>> common_symbols(1, 3, c2s)
    {'ice cube', 'light bulb', 'snowman'}
    >>> common_symbols(2, 3, c2s)
    {'ice cube', 'red lips', 'snowman', 'treble clef', 'zebra'}
    """
    answer = []
    for i in c2s:
        for word in c2s[card1]:
            if word in c2s[card2]:
                answer.append(word)

    return set(answer)

def symbol2cards(c2s):
    """
    >>> c2s = card2symbols('cards.txt')
    >>> s2c = symbol2cards(c2s)
    >>> s2c['snowman']
    {1, 2, 3, 4, 6, 8, 11}
    >>> s2c['ice cube']
    {1, 2, 3, 5, 9, 11, 12}
    >>> s2c['zebra']
    {2, 3, 4, 5, 6, 7, 8}
    """

    keyword = []
    value_number = []
    s2c = {}
    for key, value in c2s.items():
        for word in value:
            keyword.append(word)

    for i in set(keyword):
        for key, value in c2s.items():
            if i in value:
                value_number.append(key)

        s2c[i] = set(value_number)
        value_number = []
    return s2c

def common_cards(word1, word2, s2c):
    """
    >>> c2s = card2symbols('cards.txt')
    >>> s2c = symbol2cards(c2s)
    >>> common_cards('snowman', 'ice cube', s2c)
    {1, 2, 3, 11}
    >>> common_cards('ice cube', 'zebra', s2c)
    {2, 3, 5}
    >>> common_cards('zebra', 'snowman', s2c)
    {2, 3, 4, 6, 8}
    """
    answer = []
    for i in s2c:
        for word in s2c[word1]:
            if word in s2c[word2]:
                answer.append(word)

    return set(answer)

def missing_card(letter):
    """
    >>> missing_card('missing.txt')
    {'baby bottle', 'carrot', 'clown', 'daisy flower'}
    """
    answer = []
    c2s = card2symbols(letter)
    s2c = symbol2cards(c2s)
    for key, value in c2s.items():
        number = len(value)
    for key, value in s2c.items():
        if len(value) != number:
            answer.append(key)
    return set(answer)



