def alg(x):
  s = "{:b}".format(x)
  s1 = ""
  s = '0' + s
  i = len(s) - 1
  while s[i] != '0': i -= 1
  if i == 0:
    return "0"
  s = s[1:]
  i -= 1
  s = s[:i] + s[:2] + s[i+1:]
  return s[::-1]

for x in range(1,100):
  R = int(alg(x),2)
  #print(x, R)
  if R == 127:
    print('*', x, R)
    pass
