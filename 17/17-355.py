data = [ int(s) for s in open("17-354.txt") ]

max5 = max( x for x in data if abs(x) % 10 == 5 )

count, minSum = 0, 10**10
for a, b in zip(data, data[1:]):
   a2b2 = a*a + b*b
   if ((abs(a) % 10 == 8) != (abs(b) % 10 == 8)) and a2b2 > max5*max5:
      count += 1
      minSum = min( minSum, a2b2 )

print( count, minSum )

