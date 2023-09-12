number = int(input()) # number of the sentences

alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = ''
for i in range(number):
    sentence = input()
    for l in sentence:
        if l.isupper():
            l = l.lower()
            change = alphabet[-(alphabet.index(l) + 1)]
            answer += change.upper()
        elif l.islower():
            change = alphabet[-(alphabet.index(l) + 1)]
            answer += change
        elif not l.isalpha():
            answer += l
    answer += '\n'

print(answer)

