k = float(input())
p = float(input())

if p >= 10000:
    print('supergiants (a)')
elif 1000 <= p < 10000:
    print('supergiants (b)')
elif k <= 7500 and 100 <= p <1000:
    print('bright giants')
elif k <= 6000 and 10 <= p < 100:
    print('giants')
elif (k >= 3000 and p <= 0.0001) or (5000 <= k and 0.0001 <= p <= 0.01):
    print('white dwarfs')
else:
    print('main sequence')
