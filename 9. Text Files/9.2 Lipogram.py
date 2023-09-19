def occurrences(text):
    """
    >>> occurrences('lipo_01.txt')
    {'i': 21, 'm': 5, 't': 22, 'h': 8, 'n': 16, 'k': 3, 'g': 4, 'o': 12, 'f': 2, 'a': 19, 'r': 7, 'l': 6, 'q': 1, 'u': 9, 'y': 3, 'p': 1, 'c': 4, 's': 8, 'd': 6, 'w': 4, 'b': 2}
    """

    alphabet = ''
    dic = {}
    for line in open(text, 'r'):
        for letter in line:
            if letter.isalpha():
                alphabet += letter.lower()

    for letter2 in alphabet:
        dic[letter2] = alphabet.count(letter2)
    return dic

def missing_letters(text):
    """
    >>> missing_letters('lipo_01.txt')
    {'e', 'j', 'v', 'x', 'z'}
    """

    abc = 'abcdefghijklmnopqrstuvwxyz'
    answer = []
    dic = occurrences(text)
    for letter in abc:
        if letter not in dic.keys():
            answer.append(letter)

    return set(answer)

def make_lipogram(word, text, copy='X'):
    """
    >>> make_lipogram('aeiou', 'lipo_01.txt')
    'm thnkng f n rrtnl
    qntty mprtnt n clcls
    (t's hrd t dscss  ntrl
    lgrthms wtht t).
    Wht cnstnt m  thnkng f,
    nd why m  tlkng bt t
    n ths dd rndbt wy?
    >>> make_lipogram({'a', 'e', 'i', 'o', 'u'}, 'lipo_01.txt', 'copy.txt')
    """
    writer = open(copy, 'w')
    reading = open(text, 'r')
    data = reading.read()
    answer = ''

    for letter in data:
        if letter.lower() not in word and letter.upper() not in word:
            answer += letter


    for i, a in enumerate(answer.split('\n')):
        if i == len(answer.split('\n')) - 1:
            if copy == 'X':
                print(a.rstrip('\n'), end='')
            else:
                writer.write(a + '\n')
        else:
            if copy == 'X':
                print(a)
            else:
                writer.write(a + '\n')

