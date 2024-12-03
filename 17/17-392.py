data = [int(x) for x in open('17-390.txt')]

last38 = [ x for x in data if abs(x) % 100 == 38 ]
sred38 = sum(last38) / len(last38)

results = []
for i in range(len(data)-2):
  tri = data[i:i+3]
  dig3 = len( [x for x in tri if 100 <= abs(x) <= 999] )
  last3 = len( [x for x in tri if abs(x) % 10 == 3] )
  ok38 = len( [x for x in tri if x < sred38] )
  if (dig3 >= 2 and last3 == 1 and ok38 == 3 ):
    results.append( sum(tri) )

print( len(results), max(results) )
