data = [int(s) for s in open('17-403.txt')]
N = len(data)

M = min( data )
print( M )

results = []
for i in range(N - 1):
  if data[i] % 18 + data[i+1] % 18 == M :
    results.append( data[i]+data[i+1] )

print( len(results), max(results) )



