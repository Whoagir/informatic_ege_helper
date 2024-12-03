data = [int(x) for x in open('17-381.txt')]

mx39 = max( x for x in data
            if 1000<=abs(x)<10000 and abs(x) % 100 == 39 )

res = []
for a, b in zip(data, data[1:]):
  if (1000<=abs(a)<10000) + (1000<=abs(b)<10000) == 1 and (a+b)**2 <= mx39**2:
     res.append( a+b )

print( len(res), max(res) )


