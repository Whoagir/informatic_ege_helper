def alg( N ):
  s = str(N)
  sEven = ''.join( sorted((c for c in s if ord(c) % 2 == 0), reverse = True) )
  sOdd = ''.join( sorted((c for c in s if ord(c) % 2 == 1)) )
  if not sEven or not sOdd:
    return 0
  if len(sEven) > len(sOdd):
    P = sum( map(int, sEven) )
  else:
    P = sum( map(int, sOdd) )
  if P % 2 == 0:
    P = str(P) + max(sEven)
  else:
    P = str(P) + min(sOdd)
  return int(P)

count = 0
for N in range(1000,10000):
  R = alg(N)
  if R == 111:
    count += 1

print( count )

# Автор: Н. Сафронов

c = 0
for n in range(1000, 10000):
  if any(x in '13579' for x in str(n)) and any(x in '02468' for x in str(n)):
    ch = [int(x) for x in str(n) if x in '02468']
    nc = [int(x) for x in str(n) if x in '13579']
    if len(ch) > len(nc):
      R = sum(ch)
    else:
      R = sum(nc)
    if R % 2 == 0:
      R = str(R) + str(max(ch))
    else:
      R = str(R) + str(min(nc))
    if R == '111':
      c += 1
print(c)

