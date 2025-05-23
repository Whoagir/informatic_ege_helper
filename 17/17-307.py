data = [ int(x) for x in open("17-304.txt") ]
N = len(data)

def sumEven( x ):
  return sum( int(d) for d in str(x) if int(d) % 2 == 0 )
def sumOdd( x ):
  return sum( int(d) for d in str(x) if int(d) % 2 == 1 )

m = min( x for x in data if x % 2 == 1 )

def valid( a, b ):
  return sumEven(a) < sumOdd(a) and sumEven(b) < sumOdd(b) and \
         (a + b) % m == 0

count, mi = 0, None
for i in range(N-1):
   s = sum( data[i:i+2] )
   if valid( data[i], data[i+1] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

