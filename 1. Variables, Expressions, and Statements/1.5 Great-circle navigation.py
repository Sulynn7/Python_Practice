x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

import math
d = 6371 * math.acos(math.sin(x1 * math.pi / 180) * math.sin(x2 * math.pi / 180) + math.cos(x1 * math.pi / 180) * math.cos(x2 * math.pi / 180) * math.cos((y1 * math.pi / 180) - (y2 * math.pi / 180)))

print(f'The great-circle distance is {round(d)} km.')

# input = 48.87, -2.33, 37.80, 122.40