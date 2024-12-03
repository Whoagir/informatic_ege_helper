ss = 1
while True:
  s = ss
  s = s // 7
  n = 13
  while s < 255:
    if (s+n) % 2 == 0:
      s = s + 11
    n = n + 7
  if n == 90:
    print(ss)
    break
  ss += 1