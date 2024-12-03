def sumDigits( n, b = 10 ):
  s = 0
  while n:
    s += n % b
    n //= b
  return s

data = [ int(x) for x in open('17-282.txt') ]

max11 = max( x for x in data if x % 11 == 0 )
sum11 = sumDigits( max11, 3 )

count, mi = 0, 0
for i in range(len(data)-1):
  if sumDigits(data[i],3) == sum11 or sumDigits(data[i+1],3) == sum11:
    count += 1
    if not mi or data[i]+data[i+1] < mi:
      mi = data[i] + data[i+1]

print( count, mi )
