data = [ int(x) for x in open("17-304.txt") ]
N = len(data)

M = max( x for x in data if x % 246 == 0 )

def valid( a, b ):
  ha, hb = hex(a), hex(b)
  return 'aa' in ha and 'aa' in hb and \
         (a + b) < M

count, ma = 0, None
for i in range(N-1):
   s = sum( data[i:i+2] )
   if valid( data[i], data[i+1] ):
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

