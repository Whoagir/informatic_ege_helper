data = [int(x) for x in open('17-390.txt')]

max73 = max( x for x in data if abs(x) % 100 == 73 )

results = []
for i in range(len(data)-2):
  tri = data[i:i+3]
  dig3 = len( [x for x in tri if 100 <= abs(x) <= 999] )
  div11 = len( [x for x in tri if abs(x) % 11 == 0] )
  if (dig3 == 2 and div11 >= 1 and sum(tri) > max73 ):
    results.append( sum(tri) )

print( len(results), max(results) )
