data = [int(x) for x in open('17-370.txt')]

maxSum3 = max( x for x in data
              if 100 <= abs(x) < 1000 and
                 sum(map(int, str(abs(x)))) % 10 == 3 )

res = []
for a, b in zip(data,data[1:]):
  if ((1000<=abs(a)<10000) ^ (1000<=abs(b)<10000)) and \
     (a*a + b*b) % maxSum3 == 0:
     res.append( a*a + b*b )

print( len(res), max(res) )
