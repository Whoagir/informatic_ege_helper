data = [ int(x) for x in open('17-344.txt') ]
N = len(data)
mi103 = min( x for x in data if x % 103 == 0 )

def valid( a, b ):
  return (a + b) % 2 == 0 and \
         abs(a - b) % mi103 == 0

count, ma = 0, None
for i in range(N-1):
  if valid( data[i], data[i+1] ):
    count += 1
    s = sum(data[i:i+2])
    if ma == None or s > ma:
      ma = s

print( count, ma )

