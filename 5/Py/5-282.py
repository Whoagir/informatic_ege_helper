def alg(x):
  s = f"{x:b}"
  if x % 2 == 0:
    s = s + f"{s.count('1'):b}"
  else:
    s = '1' + s + '00'
  return int( s, 2 )

N = 1
while True:
  if alg(N) > 215:
    print(N)
    break
  N += 1
