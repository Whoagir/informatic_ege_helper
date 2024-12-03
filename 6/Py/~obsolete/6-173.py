ss = 1
while True:
  s = ss
  s = s // 9
  n = 4
  while s < 180:
    if (s+n) % 5 == 0:
      s = s + 7
    n = n + 9
  if n == 130:
    print(ss)
    # break
  ss += 1