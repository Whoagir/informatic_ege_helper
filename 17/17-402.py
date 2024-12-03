data = [int(s) for s in open('17-402.txt')]
N = len(data)

def sumDigits( n ):
  return sum(map(int, str(n)))

M = min( x for x in data if 10 <= x <= 99 and x % sumDigits(x) == 0 )

def valid( tri ):
  cond = [x for x in tri if x % M == 0]
  return cond

results = []
for i in range(N - 1):
  chunk = data[i:i+2]
  if valid(chunk):
    results.append( sum(chunk) )

print( len(results), max(results) )



