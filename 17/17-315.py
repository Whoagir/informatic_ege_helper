data = [ int(x) for x in open("17-304.txt") ]
N = len(data)

average = sum( data ) / N

def valid( a, b ):
  return f"{a*b:b}".count('101010') > 0 and \
         (a + b) > average

count, mi = 0, None
for i in range(N-1):
   s = sum( data[i:i+2] )
   if valid( data[i], data[i+1] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

