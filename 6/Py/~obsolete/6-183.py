count = 0
for s0 in range(1000):
    s = s0 #int(input())
    s = s * 10
    n = 3
    while s > 0:
      s = s - n
      n = n * 2
    if n == 768:
      count += 1

print( count )
