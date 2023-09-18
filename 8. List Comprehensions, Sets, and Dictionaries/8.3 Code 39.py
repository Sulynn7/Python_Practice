def reverse(dictionary):
    """
    >>> key = {'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS', 'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS', '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS', '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS', '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB', 'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB', 'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB', '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS', 'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB', '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS', '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'}
    >>> reverse(key)
    {'SbSbSbSsS': 'U', 'SsBsSbBsS': 'Z', 'BbSsSsBsS': 'P', 'SsSbBsBsS': 'R', 'SsBbBsSsS': 'H', 'SbBsSsBsS': 'W', 'SbBsSsSsB': 'D', 'BsSsSsBbS': 'K', 'SsSbBsSsB': '-', 'SbSsSbSbS': 'M', 'SsSbSsBsB': 'O', 'SsSbSbSbS': '7', 'BsSsBbSsS': '+', 'SsSsBbBsS': '1', 'SsBsBbSsS': ' ', 'SsBbSsBsS': '.', 'SsSsBsBbS': '/', 'SbSsBsBsS': 'V', 'SbSbSsSbS': 'X', 'SbSsBsSsB': 'C', 'BsSsSbBsS': 'Y', 'BsBsSsSbS': 'G', 'SsBbSsSsB': '4', 'SsBsSbSsB': 'Q', 'SsSsSsBbB': 'J', 'BsSsSbSsB': 'F', 'SsBsSsSbB': 'A', 'BsSsSsSbB': '6', 'BsBsSbSsS': '2', 'SsSsSbBsB': '$', 'BsSbBsSsS': '0', 'SsBsBsSbS': 'N', 'BsSbSsSsB': 'I', 'BbSsBsSsS': '9', 'BsSbSsBsS': 'L', 'SsSsBsSbB': ',', 'BsSsBsSbS': '5', 'BbBsSsSsS': 'B', 'SsBsSsBbS': '%', 'BsBbSsSsS': 'S', 'SbBsBsSsS': '3', 'BbSsSsSsB': 'T', 'SsSsBbSsB': '*', 'SbSsSsBsB': 'E'}
    """

    dictionary2 = {}
    for key, value in dictionary.items():
        dictionary2[value] = key
    return dictionary2

def code39(sentence, dictionary):
    """
    >>> key = {'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS', 'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS', '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS', '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS', '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB', 'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB', 'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB', '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS', 'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB', '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS', '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'}
    >>> encoded = code39('Sulfur, so good.', key)
    >>> encoded
    'BsBbSsSsSsSbSbSbSsSsBsSbSsBsSsBsSsSbSsBsSbSbSbSsSsSsSbBsBsSsSsSsBsSbBsSsBsBbSsSsBsBbSsSsSsSsSbSsBsBsSsBsBbSsSsBsBsSsSbSsSsSbSsBsBsSsSbSsBsBsSbBsSsSsBsSsBbSsBsS'
    """

    sentence2 = ''
    for l in sentence:
        for key, value in dictionary.items():
            if l.isalpha():
                if key == l.upper():
                    sentence2 += value + 's'
            else:
                if key == l:
                    sentence2 += value + 's'
    for i in range(len(sentence2)):
        sentence3 = sentence2[:-1]
    return sentence3

def decode39(encoded, dictionary):
    """
    >>> key = {'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS', 'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS', '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS', '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS', '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB', 'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB', 'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB', '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS', 'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB', '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS', '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'}
    >>> encoded = code39('Sulfur, so good.', key)
    >>> decode39(encoded, key)
    'SULFUR, SO GOOD.'
    """

    sentence = ''
    list = []
    c = 1
    d = 0
    for i in range(len(encoded) // 10 + 1):
        encoded_a = encoded[d * 10:c * 10 - 1]
        list.append(encoded_a)
        c += 1
        d += 1
    for l in list:
        for key, value in dictionary.items():
            if l == value:
                sentence += key
    return sentence
