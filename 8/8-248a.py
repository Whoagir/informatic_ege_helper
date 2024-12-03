# Автор: А. Сопов

def F(n):
  if n > 2:  return 3*F(n-1)*3 + F(n-2)
  if n == 2: return 3*F(n-1)
  if n == 1: return	1

print(4 * F(16))