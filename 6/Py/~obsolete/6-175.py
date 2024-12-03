ss = 1
while True:
  s = ss
  s = s // 5
  n = 8
  while s < 156:
    if (s+n) % 3 == 0:
      s = s + 6
    n = n + 11
  if n == 140:
    print(ss)
    # break
  ss += 1