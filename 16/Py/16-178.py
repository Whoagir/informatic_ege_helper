f = [0]*10**7
g = [0]*10**7
for n in range(10**7-1, 0, -1):
  f[n] = n if n > 2000000 else \
         7*n + f[3*n]
  g[n] = f[n] // n

print( len([ n for n in range(10**7) if g[n] == g[12345] ]) )
