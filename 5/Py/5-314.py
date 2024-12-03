def f( n ):
  s = f"{n:b}"
  if s.count('1') % 2 == 0:
    s += '0'
    s = '101' + s[3:]
  else:
    s += '11'
    s = '10' + s[2:]
  return int(s, 2)

for N in range(100):
  R = f(N)
  if R > 68:
    print( N )
    break
