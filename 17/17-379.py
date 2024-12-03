data = [int(x) for x in open('17-379.txt')]

mx15 = max( x for x in data if x % 100 == 15 )

res = []
for a, b, c in zip(data, data[1:], data[2:]):
  if (1000<=a<10000) + (1000<=b<10000) + (1000<=c<10000) == 1 and a+b+c >= mx15:
     res.append( a+b+c )

print( len(res), max(res) )


