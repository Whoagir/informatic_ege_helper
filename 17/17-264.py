data = [int(x) for x in open('17-243.txt')]

def sumDigits( n ):
  return sum( map(int, str(n)) )

ref = sum( sumDigits(x) for x in data
                          if x % 37 == 0 )
print( ref )

def nCond( arr, func ):
  b = [func(a) for a in arr]
  return b.count( True )

count, mi, ma = 0, 10**10, 0
for i, n in enumerate(data):
   if i > 0:
     pair = data[i-1:i+1]
     if nCond( pair, lambda x: x > ref ) >= 2:
        ma = max( ma, sum(pair) )
        mi = min( mi, sum(pair) )
        count += 1

print( count, mi, ma )
