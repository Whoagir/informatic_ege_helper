count = 0
for x0 in range(1000):
    x = x0 # int(input())
    a = 1
    b = a
    while a < x:
      c = a + b
      a = b
      b = c
    if b == 55:
      print( x0 )
      break
