data = [int(x) for x in open('17-390.txt')]

last13 = [ x for x in data if abs(x) % 100 == 13 ]
sred13 = sum(last13) / len(last13)

results = []
for i in range(len(data)-2):
  tri = data[i:i+3]
  dig5 = len( [x for x in tri if 10000 <= abs(x) <= 99999] )
  last7 = len( [x for x in tri if abs(x) % 10 == 7] )
  ok13 = len( [x for x in tri if x > sred13] )
  if (dig5 >= 1 and last7 == 2 and ok13 == 3 ):
    results.append( sum(tri) )

print( len(results), min(results) )
