def f( n ):
  s = f"{n:b}"
  if n % 2 == 0:
    s = '1' + s + '00'
  else:
    s = s + f"{s.count('1'):b}"
  return int(s,2)

result = (0, 10**10)
for N in range(9, 100):
  R = f(N)
  if R > 88 and R < result[1]:
    print( N, R )
    result = (N, R)
