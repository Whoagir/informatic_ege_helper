# Автор: А. Куканова

from itertools import product
even = '024'
odd = '13'

count = 0
for w in product(even + odd, repeat=5):
    w_even = [char for char in w if char in even]
    if w[0] != '0' and len(w_even) <= 3:
        count += 1
print(count)