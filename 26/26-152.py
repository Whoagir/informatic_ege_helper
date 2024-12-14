with open('26-152.txt') as F:
  N = int(F.readline())
  data = {}
  for i in range(N):
    art, price, status = map( int, F.readline().split() )
    artData = data.get( art, (price, 0, 0) )
    data[art] = (price, artData[1]+status, artData[2]+1-status)

# Средняя цена по всем товарам
sumPrice, count = 0, 0
for d in data.values():
  count += d[1]+d[2]
  sumPrice += (d[1]+d[2])*d[0]
avgPrice = sumPrice / count

# Дорогие товары
data = [ (art, *d) for art, d in data.items()
                   if d[0] > avgPrice ]

data.sort( key = lambda x: (
                 -x[3],  # продано больше всего
                 -x[1],  # наибольшая цена
                  x[2]   # осталось меньше всего
    ) )

print( data[0][1]*data[0][3], data[0][2] )