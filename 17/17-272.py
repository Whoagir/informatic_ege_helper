s = open("17-272.txt").readlines()

data = list( map( int, s ) )
dataPos = [ x for x in data if x > 0 ]

def validPair( a, b ):
  return a > avPos or b > avPos

N = len(data)
avPos = sum(dataPos)/len(dataPos)

count, maxS = 0, -100000
for i in range(N-1):
  if validPair( data[i], data[i+1] ):
    count += 1
    sum1 = sum( map(int, str(abs(data[i]))) )
    sum2 = sum( map(int, str(abs(data[i+1]))) )
    #print( data[i], data[i+1], sum1, sum2 )
    maxS = max( maxS, sum1, sum2 )

print( count, maxS )
