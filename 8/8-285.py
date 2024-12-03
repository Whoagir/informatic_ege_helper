from itertools import product

def first12( x ):
  while x:
    d = x % 12
    x //= 12
  return d

count = 0
for x in range(100000, 1000000):
  if x % first12(x) == 0:
    count += 1
print(count)

