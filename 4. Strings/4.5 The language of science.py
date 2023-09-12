word1 = input()
word2 = input()

prefix = ''
suffix = ''

for letter1, letter2 in zip(word1, word2):
    if letter1 == letter2:
        prefix += letter1
    else:
        break
for letter1, letter2 in zip(word1[::-1], word2[::-1]):
    if letter1 == letter2:
        suffix += letter1
    else:
        suffix = suffix[::-1]
        break

if not suffix:
    word1 = word1[len(prefix):]
    word2 = word2[len(prefix):]
else:
    word1 = word1[len(prefix):-len(suffix)]
    word2 = word2[len(prefix):-len(suffix)]

if len(word1) > len(word2):
    word2 = word2.center(len(word1))
elif len(word1) < len(word2):
    word1 = word1.center(len(word2))

print(' ' * len(prefix) + f'┏{word1}┓')
print(prefix + f"┫{' ' * len(word1)}┣" + suffix)
print(' ' * len(prefix) + f'┗{word2}┛')