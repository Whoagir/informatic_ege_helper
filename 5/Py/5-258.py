def alg(x):
  s0 = s = "{:b}".format(x)
  if s.count('1') % 2 == 0:
    s += '0'
  else:
    s += '1'
  if s0.count('1') > s0.count('0'):
    s += '0'
  else:
    s += '1'
  return s

count = 0
for x in range(1,30):
  R = int(alg(x),2)
  if 50 <= R <= 80:
    print(x, R)
    count += 1
print(count)