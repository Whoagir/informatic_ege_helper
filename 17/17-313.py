data = [ int(x) for x in open("17-304.txt") ]
N = len(data)

M = max( x for x in data if x % 321 == 0 )

def valid( a, b ):
  la, lb = len(hex(a)), len(hex(b))
  return la % 2 == 1 and lb % 2 == 1 and \
         (a + b) < M

count, mi = 0, None
for i in range(N-1):
   s = sum( data[i:i+2] )
   if valid( data[i], data[i+1] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

