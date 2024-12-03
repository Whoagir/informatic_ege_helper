import sys

sys.setrecursionlimit(10000)

def F( n ):
  return n if n > 3000 else 2 + F(n+2)

print( F(40) - F(43) )

# Автор: А. Рогов

f = [0] * 5000
for i in range(4000, 0, -1): # Обратный шаг
  if i > 3000:
    f[i] = i
  else:
    f[i] = f[i + 2] + 2
print(f[40] - f[43])
