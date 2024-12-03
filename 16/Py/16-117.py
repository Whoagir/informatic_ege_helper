# Автор: IIPPK

from math import log2

MAX = 500_000_000
L = int(log2(MAX)) + 1
count = 0
for n in range (0, L+1):
  for k in range (n+1, L+1):
    if 2**n + 2**k < MAX:
      count += 1
print(count)

