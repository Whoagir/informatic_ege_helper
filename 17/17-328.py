data = [int(x) for x in open("17-328.txt")]
N = len(data)

spec = [ x for x in data if x % 50 == 0 ]
M = sum(spec) / len(spec)

def isSquare( n ):
  return round(n**0.5)**2 == n

def valid( a, b, c ):
  a, b, c = sorted( [a, b, c] )
  return isSquare(a+b) and isSquare(a+c) and isSquare(b+c) and \
         a + b > M

count, mi = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

