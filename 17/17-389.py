# Автор: PRO100-ЕГЭ

data = [ int(s) for s in open("17-388.txt") ]
N = len(data)

max68 = max( x for x in data if abs(x) % 100 == 68 )

def len2( n ):
  return 10 <= abs(n) <= 99

def valid( d ):
  k = sum( len2(x) for x in d )
  return k in [1, 4] and sum(d) >= max68

results = []
for i in range(N-3):
  if valid( data[i:i+4] ):
    results.append( sum(data[i:i+4]) )

print( len(results), max(results) )
