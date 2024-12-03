s = open("17-273.txt").readlines()

data = list( map( int, s ) )
maxTotal = max(data)

def validTriple( a, b, c ):
  return a + b + c < maxTotal

N = len(data)
count, ma, mi = 0, -100000, 100000
for i in range(N-2):
  if validTriple( data[i], data[i+1], data[i+2] ):
    count += 1
    ma = max( ma, data[i], data[i+1], data[i+2] )
    mi = min( mi, data[i], data[i+1], data[i+2] )

print( count, ma+mi )
