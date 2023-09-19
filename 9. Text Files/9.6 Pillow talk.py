import string
import random

def ngrams(long_word, number):
    """
    >>> ngrams('Disgrace', 4)
    ['Disg', 'isgr', 'sgra', 'grac', 'race']
    >>> ngrams('four-year-old', 3)
    ['fou', 'our', 'yea', 'ear', 'old']
    >>> ngrams('façade', 2)
    ['fa', 'ad', 'de']
    >>> ngrams('semi-self-sustaining', 4)
    ['semi', 'self', 'sust', 'usta', 'stai', 'tain', 'aini', 'inin', 'ning']
    """
    word = ''
    word_list = []
    abc = string.ascii_letters
    c = 0
    for i, l in enumerate(long_word):
        word += long_word[i:i + number]
        if len(word) == number:
            for w in word:
                if w in abc:
                    c += 1
            if c == len(word):
                word_list.append(word)
                word = ''
                c = 0
            else:
                word = ''
                c = 0
        else:
            break

    return word_list

def dictionary(dic, number):
    """
    >>> english = dictionary('dictionary_01.txt', 3)
    >>> english['GAN']
    {'gangliglions'}
    """

    all = []
    words = []
    answer = {}
    for line in open(dic, 'r'):
        words.append(line.strip())
        ng_list = ngrams(line, number)
        for l in ng_list:
            if l.upper() not in all:
                all.append(l.upper())

    value_set = []
    for w in all:
        for l in words:
            if w in l.upper():
                value_set.append(l)
        answer[w] = set(value_set)
        value_set = []

    return answer

def ngram_count(dic, number=100):
    """
    >>> english = dictionary('dictionary_01.txt', 3)
    >>> ngram_count(english)
    44
    >>> ngram_count(english, 1)
    40
    >>> ngram_count(english, 2)
    4
    """

    c = 0
    for key, value in dic.items():
        if len(value) == number:
            c += 1
        elif number == 100:
            c += 1
    return c

def unique_ngram(dic):
    """
    >>> english = dictionary('dictionary_01.txt', 3)
    >>> unique_ngram(english)
    ('SEU', 'pseudofilaria')
    """
    one_dic = {}
    answer = []
    key_list = []
    for key, value in dic.items():
        if len(value) == 1:
            one_dic[key] = value
            key_list.append(key)

    a = random.choice(key_list)
    answer.append(a)
    answer.append(list(one_dic[a])[0])

    return tuple(answer)
