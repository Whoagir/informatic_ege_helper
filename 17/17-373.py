data = [int(x) for x in open('17-370.txt')]

def b3( n ):
  s = ''
  while n:
    s = str(n % 3) + s
    n //= 3
  return s

maxPal3 = max( x for x in data
               if 100 <= abs(x) < 1000 and
                 b3(abs(x)) == b3(abs(x))[::-1] )

res = []
for a, b in zip(data,data[1:]):
  if ((1000<=abs(a)<10000) ^ (1000<=abs(b)<10000)) and \
     (a*a + b*b) % maxPal3 == 0:
     res.append( a*a + b*b )

print( len(res), min(res) )
