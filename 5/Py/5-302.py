def alg( n ):
  s = str(n)
  if (n // 1000) % 2 == 0:
    R = int(s[0]) + int(s[2]) + abs(int(s[1]) - int(s[3]))
  else:
    s = ''.join(sorted(s))
    b = f"{int(s):b}"
    R = sum( int(d) for d in b )
  return R

count = 0
for i in range(1000, 10000):
  if alg(i) > 20:
    count += 1
print( count )