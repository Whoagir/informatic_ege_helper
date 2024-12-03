data = [int(s) for s in open('17-404.txt')]
N = len(data)

M = min( data )
print( M )

results = []
for i in range(N - 1):
  if M in [data[i] % 55, data[i+1] % 55]:
    results.append( data[i]+data[i+1] )

print( len(results), min(results) )



