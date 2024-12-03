data = [ int(x) for x in open("17-304.txt") ]
N = len(data)

def sumDig8( x ):
  s = 0
  while x:
    s += x % 8
    x //= 8
  return s

m = min( data )

def valid( a, b ):
  return ( (a % sumDig8(b) == 0) + (b % sumDig8(a) == 0) == 1 ) and \
           (a + b) % m == 0

count, ma = 0, None
for i in range(N-1):
   s = sum( data[i:i+2] )
   if valid( data[i], data[i+1] ):
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

