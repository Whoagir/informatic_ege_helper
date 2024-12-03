data = [int(x) for x in open( '17-341.txt' )]

N = len(data)
M = sum(data) / N

count, ma = 0, -10**10
for i in range(1,N-2):
  if data[i]*data[i+1] > data[i-1]*data[i+2]:
    if data[i] > M or data[i+1] > M:
      count += 1
    ma = max( ma, data[i]+data[i+1] )

print( ma, count )