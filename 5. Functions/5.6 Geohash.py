def geo2dec(letter):
    """
    >>> geo2dec('ezs42')
    14672002
    >>> geo2dec('DRUGGED')
    13684424108
    >>> geo2dec('ZUR1CH')
    1068205424
    """
    change = '0123456789bcdefghjkmnpqrstuvwxyz'
    CHANGE = '0123456789BCDEFGHJKMNPQRSTUVWXYZ'
    list = []
    for l in letter:
        if l in change:
            if l.isdigit():
                pass
            elif l.isalpha():
                list.append(change.index(l))

        if l in CHANGE:
            list.append(CHANGE.index(l))

    list = list[::-1]

    c = 0
    sum = 0
    for l in list:
        sum += (int(l) * (32 ** c))
        c += 1
    return sum

def geo2bin(letter):
    """
    >>> geo2bin('ezs42')
    '0110111111110000010000010'
    >>> geo2bin('DRUGGED')
    '01100101111101001111011110110101100'
    >>> geo2bin('ZUR1CH')
    '111111101010111000010101110000'
    """

    if len(letter) * 5 > len(bin(geo2dec(letter))):
        return bin((geo2dec(letter)))[0] + '0' * (len(letter) * 5 - len(bin(geo2dec(letter))) + 1) + bin((geo2dec(letter)))[2:]
    elif len(letter) * 5 == len(bin(geo2dec(letter))):
        return bin((geo2dec(letter)))[0] + '0' + bin((geo2dec(letter)))[2:]
    elif len(letter) * 5 < len(bin(geo2dec(letter))):
        if len(letter) * 5 == len(bin(geo2dec(letter))) - 1:
            return bin((geo2dec(letter)))[0] + bin(geo2dec(letter))[2:]
        else:
            return bin(geo2dec(letter))[2:] + '0' * (len(bin(geo2dec(letter))) - len(letter) * 5 - 2)

def unravel(number):
    """
    >>> unravel('0110111111110000010000010')
    ('0111110000000', '101111001001')
    >>> unravel('01100101111101001111011110110101100')
    ('010011001101110010', '10111110111101110')
    >>> unravel('111111101010111000010101110000')
    ('111111110000100', '111000100111100')
    """
    even = ''
    odd = ''
    for i in range(len(number)):
        if i % 2 == 0:
           even += number[i]
        if i % 2 != 0:
            odd += number[i]
    return (even, odd)

def bin2coord(number, min, max):
    for n in number:
        mid = (min + max) / 2
        if n == '1':
            min = mid
        if n == '0':
            max = mid
    return min, max

def geo2coord(letter):
    number = geo2bin(letter)
    even, odd = unravel(number)
    min, max = bin2coord(even, min=-180, max=180)
    mid1 = (min + max) / 2
    min, max = bin2coord(odd, min=-90, max=90)
    mid2 = (min + max) / 2

    return mid1, mid2


