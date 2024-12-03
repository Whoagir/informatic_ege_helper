data = [int(s) for s in open('17-407.txt')]
N = len(data)

K = sum( 1 for x in data if x % 32 == 0 )

results = []
for i in range(N - 1):
  if (data[i] < 0 or data[i+1] < 0) and \
     (data[i]+data[i+1] < K):
    results.append( data[i]+data[i+1] )

print( len(results), max(results) )



