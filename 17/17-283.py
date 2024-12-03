data = [ int(x) for x in open('17-282.txt') ]

max13 = max( x for x in data if x % 13 == 0 )

count, mi = 0, 0
for i in range(len(data)-1):
  if data[i] % max13 == 0 or data[i+1] % max13 == 0:
    count += 1
    if not mi or data[i]+data[i+1] < mi:
      mi = data[i] + data[i+1]

print( count, mi )
