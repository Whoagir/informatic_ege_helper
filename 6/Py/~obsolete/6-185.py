for s0 in range(-1000,1000):
    s = s0 # int(input())
    s = (s + 13) * 10
    n = 512
    while s < 0:
      n = n // 2
      if n == 0: break
      s = s + n
    if n == 8:
      print( s0 )
      break

