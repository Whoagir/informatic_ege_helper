def sumDigits( n ):
  return sum( map(int, str(n)) )

data = [ int(x) for x in open('17-282.txt') ]

min37 = min( x for x in data if x % 37 == 0 )
sum37 = sumDigits( min37 )

count, mi = 0, 0
for i in range(len(data)-1):
  if sumDigits(data[i]) == sum37 or sumDigits(data[i+1]) == sum37:
    count += 1
    if not mi or data[i]+data[i+1] < mi:
      mi = data[i] + data[i+1]

print( count, mi )
