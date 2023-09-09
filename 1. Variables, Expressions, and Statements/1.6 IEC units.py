x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

Ta = (x1 * 10**9) + (x2 * 10**6) + (x3 * 10**3) + x4
Tb = Ta // 2**30
Tc = (Ta % 2**30) // 2**20
Td = (Ta % 2**20) // 2**10
Te = Ta % 2**10

print(f'{Ta}b')
print(f'{Tb}Gib, {Tc}Mib, {Td}Kib, {Te}b')

# input = 2, 980, 259, 6