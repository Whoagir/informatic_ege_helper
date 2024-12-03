ss = 1
count = 0
while True:
  s = ss
  s = s // 15
  n = 14
  while s < 285:
    if (s+n) % 9 == 0:
      s = s + 11
    n = n + 13
  if n == 118:
    count += 1
    print(ss, count)
    # break
  ss += 1