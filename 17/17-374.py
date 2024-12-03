data = [int(x) for x in open('17-374.txt')]

minEven = min( x for x in data if  x % 2 == 0 )

res = []
for a, m, b in zip(data, data[1:], data[2:]):
  if ((a % 2 == 0) ^ (b % 2 == 0)) and m % minEven == 0:
    res.append( a + b )

print( len(res), min(res) )

