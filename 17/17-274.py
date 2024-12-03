s = open("17-274.txt").readlines()
data = list( map( int, s ) )

def validPair( a, b ):
  sm = abs(a) + abs(b)
  return  sm > 17043 and sm % 3 == 0

N = len(data)
count, mi = 0, 100000
for i in range(N-1):
  if validPair( data[i], data[i+1] ):
    count += 1
    mi = min( mi, data[i] + data[i+1] )

print( count, mi )
