data = [ int(x) for x in open("17-298.txt") ]

D = 197
N = len(data)

def valid( x0 ):
   x = x0
   while x:
     d = x % 10
     if d and x0 == d * D:
       return True
     x //= 10
   return False

maxD = max( x for x in data if x % D == 0 )

count, ma = 0, None
for i in range(N-1):
   s = data[i] + data[i+1]
   if (valid(data[i]) + valid(data[i+1]) == 1) \
      and s < maxD:
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

