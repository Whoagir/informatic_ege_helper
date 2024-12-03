# Автор: PRO100-ЕГЭ

data = [ int(s) for s in open("17-388.txt") ]
N = len(data)

def firstDigit( n ):
  n = abs(n)
  while n:
    d = n % 10
    n //= 10
  return d

max8 = max( x for x in data if firstDigit(x) == 8 )

def valid( d ):
  return (sum( firstDigit(x)==6 for x in d ) <= 1) and \
         sum(d) >= max8

results = []
for i in range(N-2):
  if valid( data[i:i+3] ):
    results.append( sum(data[i:i+3]) )

print( len(results), min(results) )
