a = input()
a = int(a)

k = input()
while True:
    if k != 'NYT':
        k = int(k)
    else:
        break

    b = str(input())

    if b != 'NYT':
        b = int(b)
    else:
        break

    if k + a == b:
        pass

    else:
        if b >= k:
            print(f'{k} -> {b} (+{b - k})')
        else:
            print(f'{k} -> {b} ({b - k})')

    k = b
