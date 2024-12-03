data = [int(s) for s in open('17-409.txt')]
N = len(data)

def spec( n ):
  return 1000 <= abs(n) <= 9999 and abs(n) % 10 == 7

M = max( x for x in data if spec(x) )

results = []
for i in range(N-2):
  if sum( 1 for x in data[i:i+3] if spec(x) ) >= 2 and \
     sum(data[i:i+3]) > M:
    results.append( sum(data[i:i+3]) )

print( len(results), max(results) )



