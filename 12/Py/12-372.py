# https://www.youtube.com/watch?v=uf6Jzsyzr5o&t=4896s

def alg( s ):
  while '00' not in s:
    s = s.replace('033', '1302', 1)
    s = s.replace('03', '120', 1)
    s = s.replace('023', '203', 1)
    s = s.replace('02', '20', 1)
  return s

# 33 -> 1302 -> 132 все тройки
# 3 -> 12           все единицы
# 23 -> 2           одна двойка
# 2 -> 2            одна двойка

k1, k2, k3 = 520, 786, 115

print( k2 - k3 - (k1 - k3) )
