ss = 1
while True:
  s = ss
  s = s // 9
  n = 18
  while s < 150:
    if (s+n) % 5 == 0:
      s = s + 11
    n = n + 8
  if n == 122:
    print(ss)
    break
  ss += 1