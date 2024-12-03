data = [int(s) for s in open('17-408.txt')]
N = len(data)

def spec3( n ):
  return 100 <= abs(n) <= 999 and abs(n) % 10 == 3

M = max( x for x in data if spec3(x) )

results = []
for i in range(N-2):
  if sum( 1 for x in data[i:i+3] if spec3(x) ) >= 1 and \
     sum(data[i:i+3]) < M:
    results.append( sum(data[i:i+3]) )

print( len(results), max(results) )



