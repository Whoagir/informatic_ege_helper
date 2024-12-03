def alg( n ):
  s = f"{n:b}"
  if s.count('1') % 2 == 0:
    s = s + s[-2:]
  else:
    s = s + str(1-int(s[-2])) + str(1-int(s[-1]))
  return int(s, 2)

for n in range(2, 100):
  if alg( n ) > 154:
    print( n )
    break
