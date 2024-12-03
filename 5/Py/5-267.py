def alg(x):
  s = "{:b}".format(x)
  for i, c in enumerate(s):
    if i == 0:
      sNew = c
    elif c == '0':
      sNew += '1'
    else:
      sNew += '0'
  return x + int(sNew, 2)

for x in range(100000):
  if alg(x) > 99 and x % 2 == 1:
    print(x, alg(x))
    break

