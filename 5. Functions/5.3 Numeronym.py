def numeronym(word):
    """
    >>> numeronym('internationalization')
    'i18n'
    >>> numeronym('TAKEDOWN')
    'T6N'
    >>> numeronym('Random')
    'R4m'
    >>> numeronym('DNA')
    'DNA'
    """
    if len(word) == 3:
        return word
    else:
        answer = str((word)[0] + str(len(word[1:-1])) + word[-1])
        return answer

def template(word):
    """
    >>> template('i18n')
    'i..................n'
    >>> template('TAK3N')
    'TAK...N'
    >>> template('R2D2')
    'R..D..'
    >>> template('se7en')
    'se.......en'
    """
    empty_string = ''
    for i, l in enumerate(word):
        if l.isalpha():
            empty_string += l
        else:
            if i < len(word) - 1:
                if word[i].isdigit() and word[i + 1].isdigit():
                    empty_string += '.' * int(word[i] + word[i + 1])
                elif word[i - 1].isdigit() and word[i].isdigit():
                    if i == 0:
                        empty_string += '.' * int(l)
                    else:
                        pass
                else:
                    empty_string += '.' * int(l)
            else:
                if word[i - 1].isdigit() and word[i].isdigit():
                    pass
                else:
                    empty_string += '.' * int(l)

    return empty_string

def isnumeronym(word, words):
    """
    >>> isnumeronym('i18n', 'internationalization')
    True
    >>> isnumeronym('TAK3N', 'TAKEDOWN')
    False
    >>> isnumeronym('R2D2', 'Random')
    True
    >>> isnumeronym('se7en', 'semicitizen')
    True
    """

    if word[:2].isalpha() and words[:2].isalpha():
        if word[1] == words[1]:
            if len(template(word)) == len(words):
                return True
            else:
                return False
        else:
            return False
    else:
        if len(template(word)) == len(words):
            return True
        else:
            return False