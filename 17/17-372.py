data = [int(x) for x in open('17-370.txt')]

minPal3 = min( x for x in data
               if 100 <= abs(x) < 1000 and
                 str(abs(x)) == str(abs(x))[::-1] )

res = []
for a, b in zip(data,data[1:]):
  if ((1000<=abs(a)<10000) ^ (1000<=abs(b)<10000)) and \
     (a*a + b*b) % minPal3 == 0:
     res.append( a*a + b*b )

print( len(res), max(res) )
