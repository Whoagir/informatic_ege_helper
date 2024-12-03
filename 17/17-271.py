s = open("17-271.txt").readlines()
data = list( map( int, s ) )

def validPair( a, b ):
  return abs(a) % 10 + abs(b) % 10 == 7

N = len(data)
av = sum(data)/N

count, maxS = 0, -100000
for i in range(N-1):
  if validPair( data[i], data[i+1] ):
    count += 1
    if data[i] < av and data[i+1] < av:
      maxS = max( maxS, data[i] + data[i+1] )

print( count, maxS )
