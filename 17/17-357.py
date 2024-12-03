data = [ int(s) for s in open("17-354.txt") ]

max9 = max( x for x in data if abs(x) % 10 == 9 )

count, maxSum = 0, -10**10
for a, b in zip(data, data[1:]):
   a, b = sorted( [a, b] )
   a2b2 = a*a + b*b
   if abs(b) % 10 == 2 and a2b2 < max9*max9:
      count += 1
      maxSum = max( maxSum, a2b2 )

print( count, maxSum )

