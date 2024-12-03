from itertools import product

k = 0
for n in product(range(16), repeat=3):
  if len(n) == len(set(n)) and n[0] and \
     all( (a+b) % 2 != 0 for a, b in zip(n, n[1:])) :
    k += 1

print(k)