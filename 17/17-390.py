data = [int(x) for x in open('17-390.txt')]

max15 = max( x for x in data if abs(x) % 100 == 15 )

results = []
for i in range(len(data)-2):
  tri = data[i:i+3]
  dig4 = len( [x for x in tri if 1000 <= abs(x) <= 9999] )
  div7 = len( [x for x in tri if abs(x) % 7 == 0] )
  if (dig4 == 2 and div7 >= 1 and sum(tri) > max15 ):
    results.append( sum(tri) )

print( len(results), max(results) )
