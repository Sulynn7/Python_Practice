width = int(input())
height = int(input())
depth = int(input())

depth1 = depth

c = 0
d = 1
for i in range(depth):
    q = (' ' * depth) + (':' * (width - 1)) + '/' + ('+' * c)

    if i >= height:
        print(q[:(width + depth1) - d])
        d += 1
    else:
        print(q)
    depth -= 1
    c += 1

for i in range(height):
    t = ('#' * width) + ('+' * depth1)

    if (depth1 + i) >= height:
        print(t[:(width + depth1) - d])
        d += 1
    else:
        print(t)
