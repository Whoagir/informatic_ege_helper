data = [ int(x) for x in open("17-303.txt") ]
N = len(data)

def isCube( x ):
  q = round(x**(1/3))
  return q*q*q == x

M = max( x for x in data if isCube(x) )

def valid( s ):
  diff = abs(s- M)
  return diff % 2 == 0 and diff**0.5 % 1 == 0

count, ma = 0, None
for i in range(N-2):
   a, b, c = sorted( data[i:i+3] )
   s = a + b + c
   if valid( s ):
     count += 1
     if ma == None or s > ma:
       ma = s
       res = a*b

print( count, res )

