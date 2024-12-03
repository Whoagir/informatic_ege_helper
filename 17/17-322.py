data = [int(x) for x in open("17-316.txt")]
N = len(data)

sortData = sorted(data)
sum2max = sum( sortData[-2:] )

def isSquare( n ):
  q = round(n**0.5)
  return q*q == n

def okPair( a, b ):
  return (a + b) % 2 == 0 and isSquare( a*b )

def valid( a, b, c ):
  return (okPair(a,b) or okPair(a,c) or okPair(b,c)) and \
         (a + b + c) < sum2max

count, mi = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

