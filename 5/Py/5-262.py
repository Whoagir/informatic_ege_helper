def alg(x):
  for d in [2, 3, 5]:
    if x % d == 0:
      x //= d
    else:
      x -= 1
  return x

cnt = 0
for x in range(100000):
  if alg(x) == 3:
    print(x, alg(x))
    cnt += 1

print( cnt )