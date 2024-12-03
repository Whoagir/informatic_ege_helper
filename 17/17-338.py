data = [int(x) for x in open( '17-338.txt' )]
N, M = len(data), min(data)
D = 117

count, ma = 0, 0
for i in range(N-1):
  if data[i] % D == M or data[i+1] % D == M:
    count += 1
    ma = max( ma, data[i]+data[i+1] )
print( count, ma )