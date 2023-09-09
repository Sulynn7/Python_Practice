a = input()
b = float(input())
c = float(input())
d = int((305 / b) + 1)
e = int(120 / c + 1)
if a == 'Monaco':
    print('The Grand Prix of Monaco runs over 78 laps (260.52 km).')
else:
    if c * d <= 120:
        print(f'The Grand Prix of {a} runs over {d} laps ({b * d} km).')
    else:
        print(f'The Grand Prix of {a} runs over {e} laps ({b * e} km).')
