for s0 in range(10000):
    s = (s0 + 31) // 26
    n = 813
    while s > 0:
      n = n // 3
      s = s - n
    if n == 30:
       print(s0)
       break
