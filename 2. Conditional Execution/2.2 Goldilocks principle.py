a = int(input())
b = int(input())
c = int(input())
x = input()
y = input()
d = min(b, c)
e = max(b, c)
if a > e:
    print(f'too {y}')
elif d <= a <= e:
    print('just right')
else:
    print(f'too {x}')
