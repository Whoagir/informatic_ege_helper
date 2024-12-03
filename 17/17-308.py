data = [ int(x) for x in open("17-304.txt") ]
N = len(data)

def numEven( x ):
  return len( [int(d) for d in str(x) if int(d) % 2 == 0] )
def numOdd( x ):
  return len( [int(d) for d in str(x) if int(d) % 2 == 1] )

M = max( data )

def valid( a, b ):
  return numEven(a) == numOdd(a) and numEven(b) == numOdd(b) and \
         (a + b) > M

count, ma = 0, None
for i in range(N-1):
   s = sum( data[i:i+2] )
   if valid( data[i], data[i+1] ):
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

