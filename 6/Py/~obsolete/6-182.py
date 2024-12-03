for ss in range(1000):
  s = ss
  s = (s + 21) // 10
  n = 1
  while s >= 0:
    s = s - n
    n = n * 2
  if n == 16:
    print(ss)
    break
