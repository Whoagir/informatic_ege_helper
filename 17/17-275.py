s = open("17-275.txt").readlines()
data = list( map( int, s ) )

def validPair( a, b ):
  return (a + b) % 11 == 0

N = len(data)
count, ma = 0, -100000
for i in range(N-1):
  if validPair( data[i], data[i+1] ):
    count += 1
    ma = max( ma, data[i] + data[i+1] )

print( count, ma )
