n = 1
while True:
  s = 15*'3' + 18*'2' + n*'1'
  while '31' in s or '33' in s or '21' in s:
    s = s.replace( '31', '123', 1)
    s = s.replace( '33', '211', 1)
    s = s.replace( '21', '1', 1)
  sumDigits = sum( map(int, s) )
  if sumDigits > 24:
    print( n )
    break
  n += 1

# Автор: Е. Джобс

for n in range(1,1000):
  s = '3'*15 + '2'*18 + '1'*n
  while '31' in s or '33' in s or '21' in s:
    s = s.replace( '31', '123', 1)
    s = s.replace( '33', '211', 1)
    s = s.replace( '21', '1', 1)
  if sum(map(int, s)) > 24:
    print( n )
    break
