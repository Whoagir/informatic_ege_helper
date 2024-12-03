def alg( N ):
  s = str(N)
  sEven = ''.join( sorted((c for c in s if ord(c) % 2 == 0), reverse = True) )
  sOdd = ''.join( sorted((c for c in s if ord(c) % 2 == 1)) )
  if not sEven or not sOdd:
    return float('inf')
  return int(sEven) + int(sOdd)

results = []
for N in range(1000,10000):
  R = alg(N)
  s = str(R)
  if R > 10 and all( s[i]>s[i+1] for i in range(len(s)-1)):
    results.append( R )

print( max(results) )

# Автор: Н. Сафронов

a = []
for n in range(1000, 10000):
  if any(x in '13579' for x in str(n)) and any(x in '02468' for x in str(n)):
    ch = ''.join(sorted([x for x in str(n) if x in '02468'], reverse=True))
    nc = ''.join(sorted([x for x in str(n) if x in '13579']))
    R = str(int(ch) + int(nc))
    if int(R) > 10 and all(R[i] > R[i+1] for i in range(len(R)-1)):
      a.append( int(R) )
print(max(a))

