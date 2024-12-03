data = [int(x) for x in open('17-390.txt')]

last28 = [ x for x in data if abs(x) % 100 == 28 ]
sred28 = sum(last28) / len(last28)

results = []
for i in range(len(data)-2):
  tri = data[i:i+3]
  dig4 = len( [x for x in tri if 1000 <= abs(x) <= 9999] )
  last11 = len( [x for x in tri if abs(x) % 100 == 11] )
  ok28 = len( [x for x in tri if x > sred28] )
  if (dig4 >= 1 and last11 == 2 and ok28 == 3 ):
    results.append( sum(tri) )

print( len(results), min(results) )
