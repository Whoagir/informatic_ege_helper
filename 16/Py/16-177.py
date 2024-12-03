f = [0]*10**7
g = [0]*10**7
for n in range(10**7-1, 0, -1):
  f[n] = n if n > 1000000 else \
         3*n + f[5*n]
  g[n] = f[n] // n

print( len([ n for n in range(10**7) if g[n] == g[3000] ]) )
