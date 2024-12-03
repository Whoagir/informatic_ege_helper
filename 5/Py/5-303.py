def alg( n ):
  s = str(n)
  if s[0] in '48':
    s = '9' + s[1:]
  elif s[0] in '26':
    s = '3' + s[1:]
  return int(s)

count = 0
for i in range(1000, 10000):
  R = alg(i)
  if R // 1000 == 9 and R % 8 == 4:
    count += 1
print( count )