def outside(letter):
    """
    >>> outside('quick')
    'qk'
    >>> outside('queen')
    'qn'
    >>> outside('king')
    'kg'
    >>> outside('win')
    'wn'
    """
    return letter[0] + letter[-1]

def inside(letter):
    """
    >>> inside('quick')
    'uic'
    >>> inside('queen')
    'uee'
    >>> inside('king')
    'in'
    >>> inside('win')
    'i'
    """
    return letter[1:-1]

def issubword(subword, letter):
    """
    >>> issubword('quick', 'qwertyuihgfcvbnhjk')
    True
    >>> issubword('win', 'qwertyuytresdftyuiokn')
    True
    >>> issubword('queen', 'qwertyuytresdftyuiokn')
    True
    >>> issubword('quick', 'qwertyuytresdftyuiokn')
    False
    """
    list1 = []

    c = 0
    for i, a in enumerate(letter):
        while True:
            if c < len(subword):
                if a == subword[c]:
                    list1.append(i)
                    c += 1
                else:
                    break
            else:
                break

    for b in subword:
        if b not in letter:
            return False
    if len(list1) != len(subword):
        return False
    elif list1 == sorted(list1):
        return True
    else:
        return False

def iswandering(subword, letter):
    """
    >>> iswandering('quick', 'qwertyuihgfcvbnhjk')
    True
    >>> iswandering('win', 'qwertyuytresdftyuiokn')
    False
    >>> iswandering('queen', 'qwertyuytresdftyuiokn')
    True
    >>> iswandering('quick', 'qwertyuytresdftyuiokn')
    False
    """
    if outside(subword) == outside(letter):
        if issubword(subword, letter) == True:
            return True
        else:
            return False
    else:
        return False

def read_dictionary(dictionary):
    """
    >>> dictionary = read_dictionary('dictionary.txt')
    >>> dictionary['qk']
    {'uir', 'uar', 'uarterdec', 'uac', 'uarterbac', 'uic'}
    >>> dictionary['qn']
    {'uotidia', 'uee', 'uestio', 'uicke'}
    >>> dictionary['xx']
    Traceback (most recent call last):
    KeyError: 'xx'
    """
    dic = {}
    for line in open(dictionary, 'r'):
        letter = line.rstrip('\n')
        in_line = [inside(letter)]
        if outside(letter) in dic:
            to_list = list(dic[outside(letter)])
            new_list = to_list + in_line
            dic[outside(letter)] = set(new_list)
        else:
            dic[outside(letter)] = set(in_line)

    return dic


def wanderings(letter, dictionary):
    """
    >>> dictionary = read_dictionary('dictionary.txt')
    >>> wanderings('qwertyuihgfcvbnhjk', dictionary)
    {'quick'}
    >>> wanderings('qwertyuytresdftyuiokn', dictionary)
    {'queen', 'question'}
    >>> wanderings('ghijakjthoijerjidsdfnokg', dictionary)
    {'gating', 'geeing', 'goring', 'going', 'gathering'}
    >>> wanderings('xkzjunspebfgslddfksdrx', dictionary)
    set()
    """
    answer = []
    letter2 = outside(letter)
    if letter2 in dictionary:
        for word in dictionary[letter2]:
            word2 = letter2[0] + word + letter2[-1]
            if iswandering(word2, letter) == True:
                answer.append(word2)
            else:
                pass

        return set(answer)
    else:
        return set()
