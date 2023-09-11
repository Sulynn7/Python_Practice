n = int(input())
plus_value = int(input())
double = int(input())
last_table = input()

value = 0
profit = 0

for i in range(1, n + 1):
    if i == n and last_table == 'lost':
        print(f'table #{i}: €{int(profit / 2)}')
        break

    value += plus_value

    profit += value

    if i % double == 0:
        profit *= 2
        print(f'table #{i} (x2): €{profit}')

    else:
        print(f'table #{i}: €{profit}')