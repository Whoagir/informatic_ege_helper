data = [int(x) for x in open( '17-339.txt' )]
N, M = len(data), min( x for x in data if x > 0 and x % 19 == 0 )

count, ma = 0, 0
for i in range(N-1):
  if data[i] + data[i+1] < M:
    count += 1
    ma = max( ma, data[i]+data[i+1] )
print( count, abs(ma) )