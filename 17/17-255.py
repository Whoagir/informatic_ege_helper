data = [int(x) for x in open('17-243.txt')]

ref = max( x for x in data if x % 173 == 0 )

def nCond( arr, func ):
  b = [func(a) for a in arr]
  return b.count( True )

def toBase( n, base ):
  s = ''
  while n:
    s = str(n%base) + s
    n //= base
  return s

count, mi, ma = 0, 10**10, 0
for i, n in enumerate(data):
   if i > 0:
     pair = data[i-1:i+1]
     if nCond( pair, lambda x: x > ref ) >= 1 and \
        nCond( pair, lambda x: '22' in toBase(x,3) ) >= 1:
        ma = max( ma, sum(pair) )
        mi = min( mi, sum(pair) )
        count += 1

print( count, mi )
