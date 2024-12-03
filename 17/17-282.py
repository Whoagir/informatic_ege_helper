data = [ int(x) for x in open('17-282.txt') ]

min17 = min( x for x in data if x % 17 == 0 )

count, ma = 0, 0
for i in range(len(data)-1):
  if data[i] % min17 == 0 or data[i+1] % min17 == 0:
    count += 1
    ma = max( ma, data[i]+data[i+1] )

print( count, ma )
