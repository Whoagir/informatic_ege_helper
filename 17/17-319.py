data = [int(x) for x in open("17-316.txt")]
N = len(data)

average = sum( data ) / N

def okPair( a, b ):
  return (a // 1000 + b // 1000) == (a % 10 + b % 10)

def valid( a, b, c ):
  return (okPair(a,b) or okPair(a,c) or okPair(b,c)) and \
         (a + b + c) / 3 > average

count, ma = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

