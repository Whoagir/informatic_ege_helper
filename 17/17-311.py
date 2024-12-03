data = [ int(x) for x in open("17-304.txt") ]
N = len(data)

M = max( x for x in data if x % 120 == 0 )

def valid( a, b ):
  ca, cb = hex(a).count('a'), hex(b).count('a')
  return ca > 0 and ca % 2 == 0 and cb > 0 and cb % 2 == 0 and \
         (a + b) > M

count, mi = 0, None
for i in range(N-1):
   s = sum( data[i:i+2] )
   if valid( data[i], data[i+1] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

