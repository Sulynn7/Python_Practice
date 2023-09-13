def pigword(letter):
    """
    >>> pigword('egg')
    'eggway'
    >>> pigword('Pig')
    'Igpay'
    >>> pigword('Latin')
    'Atinlay'
    >>> pigword('trash')
    'ashtray'
    >>> pigword('quit')
    'itquay'
    >>> pigword('BaNaNa')
    'ANaNabay'
    >>> pigword('DNa')
    'AdNay'
    >>> pigword('plover')
    'overplay'
    >>> pigword('plunder')
    'underplay'
    """
    a1 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if letter[0] in a1:
        letter2 = str(letter) + 'way'
        return str(letter2)
    elif len(letter) == 1:
        if letter in a1:
            return str(str(letter) + 'way')
        else:
            return str(str(letter) + 'ay')
    else:
        for i, n in enumerate(letter):
            if n in a1:
                if not(n == 'u' and letter[i - 1] == 'q'):
                    letter3 = letter[i:] + letter[0].lower() + letter[1:i] + 'ay'
                    letter5 = letter[i:] + letter[0].upper() + letter[1:i] + 'ay'
                    if letter[0].isupper() and letter[i].islower():
                        letter4 = letter3[0].upper() + letter3[1:]
                        return str(letter4)
                    elif letter[0].isupper() and letter[i].isupper():
                        letter4 = letter3[0].upper() + letter5[1:]
                        return str(letter4)
                    else:
                        return str(letter3)
        return letter + 'ay'

def piglatin(letter):
    """
    >>> piglatin('And now for something completely different!')
    'Andway ownay orfay omethingsay ompletelycay ifferentday!'
    >>> piglatin('Stwike him, centuwion, stwike him vewy wuffly')
    'Ikestway imhay, entuwioncay, ikestway imhay ewyvay ufflyway'
    """
    word = ''
    word2 = ''
    word3 = ''
    for i, n in enumerate(letter + ' '):
        if n.isalpha():
            word += n
        elif not n.isalpha():
            word2 += n
            if word == '' and (word2 == ' ' or word2 == '.' or word2 == '-' or word2 == "'" or word2 == '(' or word2 == ')'):
                word3 += word2
            else:
                word3 += pigword(word) + str(word2)
            word = ''
            word2= ''

    return word3.rstrip()