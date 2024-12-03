data = [int(s) for s in open('17-403.txt')]
N = len(data)

M = min( data )
print( M )

B = 65
results = []
for i in range(N - 1):
  if data[i] % B == M and data[i+1] % B == M:
    results.append( data[i]+data[i+1] )

print( len(results), max(results) )



