ss = 1
while True:
  s = ss
  s = s // 7
  n = 15
  while s < 211:
    if (s+n) % 5 == 0:
      s = s + 11
    n = n + 13
  if n == 119:
    print(ss)
    # break
  ss += 1