data = [int(x) for x in open('17-390.txt')]

last = [ x for x in data if abs(x) % 1000 == 271 ]
sred = sum(last) / len(last)

results = []
for i in range(len(data)-2):
  tri = data[i:i+3]
  dig3 = len( [x for x in tri if 100 <= abs(x) <= 999] )
  div11 = len( [x for x in tri if abs(x) % 11 == 0] )
  div3 = len( [x for x in tri if abs(x) % 3 == 0] )
  okEnd = len( [x for x in tri if x > sred] )
  if ( 1<= dig3 <= 2 and div11 > div3 and okEnd == 3 ):
    results.append( sum(tri) )

print( len(results), min(results) )
