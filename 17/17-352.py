data = [ int(x) for x in open('17-352.txt') ]

max73 = max( x for x in data if x % 73 == 0 )

pairSums = []
for x, y in zip(data, data[1:]):
   if x >= max73 and y >= max73:
     pairSums.append( x + y )

print( len(pairSums), max(pairSums) )