data = [ int(x) for x in open("17-302.txt") ]
N = len(data)

M = min( x for x in data if x % 21 == 0 )

def valid( a, b ):
  return abs((a+b)/2 - M)**0.5 % 1 == 0

count, mi = 0, None
for i in range(N-1):
   s = data[i]*data[i+1]
   if valid(data[i], data[i+1]):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

