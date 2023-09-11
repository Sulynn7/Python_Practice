a = int(input())

while True:
    b = input()

    if b == 'stop':
        print(f'You end up with {a} dollar.')
        break
    elif b == 'all':
        b = a
        a -= b
    else:
        b = int(b)
        if a < b:
            if a != 0:
                print(f'You cannot bet {b} dollar if you only have {a} dollar.')
            else:
                print(f'You end up with 0 dollar.')

            break
        a -= b

    c = input()
    d = input()

    if c == d:
        a += 2 * b

    else:
        pass



