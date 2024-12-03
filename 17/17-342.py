data = [int(x) for x in open( '17-342.txt' )]
N = len(data)

mi37 = min( x for x in data if x % 37 == 0 )
ma73 = max( x for x in data if x % 73 == 0 )
m = min( mi37, ma73 )
M = max( mi37, ma73 )

def valid( a, b ):
  return ( (m < a < M) + (m < b < M) ) == 1

count, mi = 0, 10**10
for i in range(0,N-1):
  if valid( data[i], data[i+1] ):
    count += 1
    mi = min( mi, data[i]+data[i+1] )

print( count, mi )