data = [ int(x) for x in open('17-281.txt') ]

def arif( d ):
  q = d[1] - d[0]
  return q if q > 0 and d[2] - d[1] == q else \
         0
def geom( d ):
  q = d[1] // d[0]
  return q if q > 0 and d[2] // d[1] == q else \
         0

count, ma = 0, 0
for i in range(len(data)-6):
  q1, q2 = arif(data[i:i+3]), geom(data[i+3:i+6])
  if q1*q2 == 0:
    q1, q2 = geom(data[i:i+3]), arif(data[i+3:i+6])
  if q1*q2 > 0 and q1 == q2:
    count += 1
    ma = max( ma, sum(data[i:i+6]) )

print( count, ma )
