# Автор: А. Сандарян

mi = None
for N in range(1,1000):
  for M in range(1,1000):
    N1 = bin(N)[2:].count('1')**2
    M1 = bin(M)[2:].count('1')**2
    if N1 - M1 == 33 and \
       (mi == None or N+M < mi):
      mi = N + M

print( mi )