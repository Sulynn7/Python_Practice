def letter_frequencies(frequentie):
    """
    >>> frequentie = letter_frequencies("fifteen e's, seven f's, four g's, six h's, eight i's, four n's, five o's, six r's, eighteen s's, eight t's, four u's, three v's, two w's, three x's")
    >>> frequentie['e']
    15
    >>> frequentie['f']
    7
    >>> frequentie['g']
    4
    >>> frequentie = letter_frequencies("sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's")
    >>> frequentie['e']
    16
    >>> frequentie['f']
    5
    >>> frequentie['g']
    3
    """

    c = 0
    k = {}
    frequentie2 = frequentie.lower()
    frequentie3 = set(frequentie2)
    for l in frequentie3:
        if l.isalpha():
            for s in frequentie2:
                if l == s:
                    c += 1
            k[l] = c
            c = 0
    return k

def letter_positions(frequentie):
    """
    >>> positions = letter_positions("fifteen e's, seven f's, four g's, six h's, eight i's, four n's, five o's, six r's, eighteen s's, eight t's, four u's, three v's, two w's, three x's")
    >>> positions['e']
    {4, 5, 8, 14, 16, 43, 67, 83, 88, 89, 97, 121, 122, 141, 142}
    >>> positions['f']
    {0, 2, 19, 24, 54, 64, 108}
    >>> positions['g']
    {29, 45, 85, 99}

    >>> positions = letter_positions("sixteen e's, five f's, three g's, six h's, nine i's, five n's, four o's, six r's, eighteen s's, eight t's, three u's, three v's, two w's, four x's")
    >>> positions['e']
    {4, 5, 8, 16, 26, 27, 46, 56, 82, 87, 88, 96, 110, 111, 121, 122}
    >>> positions['f']
    {13, 18, 53, 63, 138}
    >>> positions['g']
    {29, 84, 98}
    """

    c = []
    k = {}
    frequentie2 = frequentie.lower()
    for l in set(frequentie2):
        if l.isalpha():
            for i, s in enumerate(frequentie2):
                if l == s:
                    c.append(i)
            k[l] = set(c)
            c = []
    return k

