for ss in range(1000):
  s = ss
  s = (s - 21) // 10
  n = 1
  while s >= 0:
    n = n * 2
    s = s - n
  if n == 8:
    print(ss)
    break
