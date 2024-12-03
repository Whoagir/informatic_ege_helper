data = [ int(s) for s in open("17-354.txt") ]

min2 = min( x for x in data if abs(x) % 10 == 2 )

count, minSum = 0, 10**10
for a, b in zip(data, data[1:]):
   a2b2 = a*a + b*b
   if abs(abs(a) % 10 - abs(b) % 10) == 1 and \
      ((a % 5 == 0) != (b % 5 == 0)) and  a2b2 > min2*min2:
      count += 1
      if a + b > 0:
        minSum = min( minSum, a+b )

print( count, minSum )

