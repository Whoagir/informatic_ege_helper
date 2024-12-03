data = [int(x) for x in open('17-1.txt')]

average = sum(data) / len(data)

def nCond( arr, func ):
  b = [func(a) for a in arr]
  return b.count( True )

count, ma = 0, 0
for i, n in enumerate(data):
   if i > 1:
     triple = data[i-2:i+1]
     if nCond( triple, lambda x: x < average ) >= 2 and\
        nCond( triple, lambda x: abs(x) % 100 == 14 ) >= 1:
        ma = max( ma, sum(triple) )
        count += 1

print( count, ma )
