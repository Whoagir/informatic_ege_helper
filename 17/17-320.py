data = [int(x) for x in open("17-316.txt")]
N = len(data)

max202 = max( x for x in data if x % 202 == 0 )

def okPair( a, b ):
  return a % 2 == 0 and b % 2 == 0 and \
         (a + b) % 100 == 44

def valid( a, b, c ):
  return (okPair(a,b) or okPair(a,c) or okPair(b,c)) and \
         (a + b + c) > max202

count, mi = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

