ss = 1
while True:
  s = ss
  s = s // 7
  n = 11
  while s < 130:
    if (s+n) % 3 == 0:
      s = s + 7
    n = n + 13
  if n == 102:
    print(ss)
    break
  ss += 1