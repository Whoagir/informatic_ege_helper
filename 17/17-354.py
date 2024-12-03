data = [ int(s) for s in open("17-354.txt") ]

min3 = min( x for x in data if abs(x) % 10 == 3 )

count, maxSum = 0, -10**10
for a, b in zip(data, data[1:]):
   a2b2 = a*a + b*b
   if ((abs(a) % 10 == 3) != (abs(b) % 10 == 3)) and a2b2 < min3*min3:
      count += 1
      maxSum = max( maxSum, a2b2 )

print( count, maxSum )

