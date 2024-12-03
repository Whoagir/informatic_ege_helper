data = [ int(x) for x in open('17-353.txt') ]

sred = (max(data) + min(data)) / 2

pairSums = []
L, R = 0, len(data)-1
while L < R:
  if data[L] > sred and data[R] < sred or \
     data[R] > sred and data[L] < sred:
    pairSums.append( data[L] + data[R] )
  L, R = L+1, R-1

print( len(pairSums), max(pairSums) )