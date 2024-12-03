ss = 1
count = 0
while True:
  s = ss
  s = s // 9
  n = 12
  while s < 220:
    if (s+n) % 3 == 0:
      s = s + 7
    n = n + 17
  if n == 131:
    count += 1
    print(ss, count)
    # break
  ss += 1