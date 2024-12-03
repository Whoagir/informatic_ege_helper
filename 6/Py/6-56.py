from math import ceil

a = 400
x1 = a + a*2**0.5
b1 = x1
y1 = a/2**0.5

print( x1, y1 )

count = 0
for x in range(1, ceil(x1)):
  for y in range(1, ceil(y1)):
    if y < x and y < - x + b1:
       count += 1

print( count )