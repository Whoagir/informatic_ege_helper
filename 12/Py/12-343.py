# Автор: Е. Джобс

n = 20
s = '321'*n + '2'*20 + '1'*20
while '23' in s or '32' in s or '12' in s:
  s = s.replace('12', '21', 1)
  s = s.replace('32', '1', 1)
  s = s.replace('23', '2', 1)

print( sum(map(int, s)) )
