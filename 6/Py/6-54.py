from fractions import *

def lineParams( x1, y1, x2, y2 ):
  # (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)
  # y = y1 + (y2 - y1)*(x - x1)/(x2 - x1)
  # y = ((y2 - y1)/(x2 - x1)) * x + y1 - x1*(y2 - y1)/(x2 - x1)
  return Fraction( y2-y1, x2-x1 ),  \
         y1 - x1*Fraction( y2-y1, x2-x1 )

k1, b1 = lineParams( 0, 0, 200, 100 )
k2, b2 = lineParams( 200, 100, 150, -50 )
k3, b3 = lineParams( 150, -50, 0, 0 )

count = 0
for x in range(201):
  for y in range(-50, 101):
     if y <= k1*x+b1 and y >= k2*x+b2 and y >= k3*x+b3:
        count += 1

print( count )