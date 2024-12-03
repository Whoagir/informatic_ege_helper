# Автор: А. Носкин

from math import *
count = 0
k = tan(radians(30))  # tg угла 30 градусов
for x in range(1, 10):
  for y in range(1, 10):
    if y < -k * x + 8 and y < k*x +4 and x<7:
      count += 1
print(count)


