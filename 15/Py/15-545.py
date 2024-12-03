def ДЕЛ( x, d ): return x % d == 0

for A in range(500):
  if all( (ДЕЛ(x, 10) and ДЕЛ(x, 26) and (x >= 300)) <= (A <= x)
          for x in range(1000)):
    print(A)
