data = [ int(s) for s in open('17-384.txt') ]

maxPair = max( a+b for a, b in zip(data, data[1:])
                   if (10<=a<=99)+(10<=b<=99) == 1 )

res = [ x for x in data if x > maxPair ]

print( len(res), min(res) )