def alg(x):
  for d in [2, 3, 7]:
    if x % d == 0:
      x //= d
    else:
      x -= 1
  return x

cnt = 0
for x in range(100000):
  if alg(x) == 2:
    print(x, alg(x))
    cnt += 1

print( cnt )