# https://www.youtube.com/watch?v=y7N-5jX99X0

f, fPrev = 1, 0
for i in range(2, 20+1):
  f, fPrev = f+fPrev, f
  print( i, f, fPrev )

print( 2*f )