data = [int(x) for x in open("17-316.txt")]
N = len(data)

average = sum( data ) / N

def isOkPair( a, b ):
  n = a + b
  digits = [ int(d) for d in str(n) ]
  q = round(n**0.5)
  return q*q == n

def valid( a, b, c ):
  return (isOkPair(a,b) or isOkPair(b,c) or isOkPair(c,a)) and \
         (a + b + c) / 3 > average

count, ma = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

