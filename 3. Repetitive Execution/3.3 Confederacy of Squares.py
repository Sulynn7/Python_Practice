from datetime import date
d = date.today().year

a = input()
b = int(input())
c = 0

while True:
    b += 1
    c += 1

    if b != (c ** 2):
        if c > 100:
            print(f'{a} is not a member of the Confederacy of Squares.')
            break
    else:
        if b >= d:
            print(f'{a} turns {c} in {b}.')
            break
        elif b < d:
            print(f'{a} was {c} in {b}.')
            break

