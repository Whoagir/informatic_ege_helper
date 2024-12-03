
N = 64
while True:
  s = f"{N:o}"
  if N % 5 == 0:
    s += s[:3]
  else:
    s += f"{N%5:b}"
  R = int( s, 8 )
  if R >= 35000: break
  N += 1


print( N )