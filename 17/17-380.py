data = [int(x) for x in open('17-380.txt')]

mx25 = max( x for x in data if abs(x) % 100 == 25 )

res = []
for a, b, c in zip(data, data[1:], data[2:]):
  if (1000<=abs(a)<10000) + (1000<=abs(b)<10000) + (1000<=abs(c)<10000) <= 2 and a+b+c <= mx25:
     res.append( a+b+c )

print( len(res), max(res) )


