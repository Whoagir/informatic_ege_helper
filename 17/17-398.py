data = [int(x) for x in open('17-390.txt')]

last = [ x for x in data if abs(x) % 1000 == 151 ]
sred = sum(last) / len(last)

results = []
for i in range(len(data)-2):
  tri = data[i:i+3]
  dig4 = len( [x for x in tri if 1009 <= abs(x) <= 9999] )
  div13 = len( [x for x in tri if abs(x) % 13 == 0] )
  div7 = len( [x for x in tri if abs(x) % 7 == 0] )
  okEnd = len( [x for x in tri if x > sred] )
  if ( 1<= dig4 <= 2 and div13 > div7 and okEnd == 3 ):
    results.append( sum(tri) )

print( len(results), min(results) )
