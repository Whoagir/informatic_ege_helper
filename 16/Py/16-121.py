from math import log2

MAX = 1_000_000_000

Lmax = int(log2(MAX)) + 1
count = 0
for L in range(Lmax,2,-1):
  for n in range (0, L-1):
    for k in range (n+1, L-1):
      for m in range (k+1, L-1):
        if 2**L - 1 - 2**n - 2**k - 2**m < MAX:
          count += 1
print(count)

"""
count = 0
for n in range (MAX):
   s = f"{n:b}"
   if s.count('0') == 3:
      count += 1
print(count)

def f( n ):
  return 6 if n == 0 else \
         1+f(n//2) if n % 2 == 0 else \
         f(n//2)

count = 0
for i in range(MAX):
  if f(i) == 9:
    count += 1
print( count )
"""