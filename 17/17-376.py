data = [int(x) for x in open('17-376.txt')]

max0F = max( x for x in data if x % 256 == 15 )

res = []
for a, b in zip(data, data[1:]):
  if ((a % 7 == 0) ^ (b % 7 == 0)) and (a + b) % max0F == 0:
    res.append( a + b )

print( len(res), max(res) )
