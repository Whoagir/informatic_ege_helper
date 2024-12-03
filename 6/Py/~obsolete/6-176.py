ss = 1
count = 0
while True:
  s = ss
  s = s // 11
  n = 9
  while s < 203:
    if (s+n) % 5 == 0:
      s = s + 6
    n = n + 13
  if n == 126:
    count += 1
    print(ss, count)
    # break
  ss += 1