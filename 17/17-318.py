data = [int(x) for x in open("17-316.txt")]
N = len(data)

sortData = sorted(data)
sum2 = sum( sortData[-2:] )

def okPair( a, b ):
  count = 0
  while a:
    if a % 10 == b % 10: count += 1
    a, b = a//10, b//10
  return count == 1

def valid( a, b, c ):
  return (okPair(a,b) or okPair(a,c) or okPair(b,c)) and \
         (a + b + c) < sum2

count, mi = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

