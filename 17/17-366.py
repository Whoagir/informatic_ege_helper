data = [ int(x) for x in open('17-366.txt') ]

min68 = min( x for x in data if abs(x) % 100 == 68 )

N = len(data)

res = []
for i in range(N-1):
  if ((abs(data[i]) % 100 == 68) ^ (abs(data[i+1]) % 100 == 68)) and \
      data[i]**2 + data[i+1]**2 >= min68**2:
    res.append( data[i]**2 + data[i+1]**2 )

print( len(res), max(res) )