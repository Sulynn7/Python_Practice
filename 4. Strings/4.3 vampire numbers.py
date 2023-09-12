a = int(input())
b = 1
s = 0

while True:
    c = a / b
    if int(c) * b == a:
        s += 1
        if len(str(a)) % 2 == 0:
            s += 1
            if len(str(b)) == len(str(int(c))):
                s += 1
                t = sorted(str(b))
                p = sorted(str(int(c)))
                if sorted(t + p) == sorted(str(a)):
                    s += 1
                    if a % 100 != 0:
                        s += 1
                    else:
                        pass
        else:
            print(f'{a} is not a vampire number.')
            break

    if s == 5:
        print(f'{a} is a vampire number.')
        break
    elif b == a:
        print(f'{a} is not a vampire number.')
        break
    else:
        b += 1
        s = 0
