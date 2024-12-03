def sumDigits( n, b = 10 ):
  s = 0
  while n:
    s += n % b
    n //= b
  return s

data = [ int(x) for x in open('17-282.txt') ]

min21 = min( x for x in data if x % 21 == 0 )
sum21 = sumDigits( min21, 8 )

count, mi = 0, 0
for i in range(len(data)-1):
  if sumDigits(data[i],8) == sum21 or sumDigits(data[i+1],8) == sum21:
    count += 1
    if not mi or data[i]+data[i+1] < mi:
      mi = data[i] + data[i+1]

print( count, mi )
