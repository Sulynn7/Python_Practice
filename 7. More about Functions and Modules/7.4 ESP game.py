import random

def taboo_length(words, minimum=0, maximum=100):
    """
    >>> words = ['forest', 'meadow', 'scenery', 'hills']
    >>> taboo_length(words)
    3
    >>> taboo_length(words, minimum=2)
    4
    >>> taboo_length(words, maximum=3)
    1
    >>> taboo_length(words, minimum=2, maximum=3)
    3
    >>> taboo_length(words, minimum=-2, maximum=6)
    1
    """
    if minimum <= 0:
        minimum = 0
        if maximum <= len(words):
            if maximum < 0:
                maximum = len(words)
                return random.randint(minimum, maximum)
            else:
                return random.randint(minimum, maximum)
        if maximum > len(words):
            maximum = len(words)
            return random.randint(minimum, maximum)
        if maximum == 100:
            maximum = len(words)
            return random.randint(minimum, maximum)
    if minimum > len(words):
        minimum = 0
        if maximum <= len(words):
            if maximum < 0:
                maximum = len(words)
                return random.randint(minimum, maximum)
            else:
                return random.randint(minimum, maximum)
        if maximum > len(words):
            maximum = len(words)
            return random.randint(minimum, maximum)
        if maximum == 100:
            maximum = len(words)
            return random.randint(minimum, maximum)
    if minimum < len(words):
        if maximum <= len(words):
            if maximum <= 0:
                maximum = len(words)
                return random.randint(minimum, maximum)
            else:
                return random.randint(minimum, maximum)
        if maximum > len(words):
            maximum = len(words)
            return random.randint(minimum, maximum)
        if maximum == 100:
            maximum = len(words)
            return random.randint(minimum, maximum)

    return random.randint(minimum, maximum)

def taboo_words(words, minimum=0, maximum=100):
    """
    >>> words = ['forest', 'meadow', 'scenery', 'hills']
    >>> taboo_words(words)
    ['forest', 'hills', 'meadow', 'scenery']
    >>> taboo_words(words, minimum=2)
    ['forest', 'meadow', 'scenery']
    >>> taboo_words(words, maximum=3)
    ['forest', 'hills', 'meadow']
    >>> taboo_words(words, minimum=2, maximum=3)
    ['hills', 'meadow', 'scenery']
    >>> taboo_words(words, minimum=-2, maximum=6)
    ['forest', 'hills', 'meadow', 'scenery']
    """

    a = taboo_length(words, minimum, maximum)
    b = random.sample(words, a)
    c = []
    e = []
    for l in b:
        l = l.lower()
        c.append(l)
    d = sorted(c)
    for s in d:
        for t in words:
            if s == t.lower():
                s = t
                e.append(t)
    return e
