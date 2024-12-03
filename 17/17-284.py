data = [ int(x) for x in open('17-282.txt') ]

max41 = max( x for x in data if x % 41 == 0 )

count, ma = 0, 0
for i in range(len(data)-1):
  if (data[i] + data[i+1]) < max41:
    count += 1
    ma = max( ma, data[i]+data[i+1] )

print( count, ma )
