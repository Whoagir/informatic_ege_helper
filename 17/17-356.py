data = [ int(s) for s in open("17-354.txt") ]

min1 = min( x for x in data if abs(x) % 10 == 1 )

count, maxSum = 0, -10**10
for a, b in zip(data, data[1:]):
   a, b = sorted( [a, b] )
   a2b2 = a*a + b*b
   if abs(a) % 10 == 4 and a2b2 < min1*min1:
      count += 1
      maxSum = max( maxSum, a2b2 )

print( count, maxSum )

