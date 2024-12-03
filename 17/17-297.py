data = [ int(x) for x in open("17-297.txt") ]

N = len(data)
max51 = max( x for x in data if x % 51 == 0 )

def valid51( x ): return x == (x%10) * 51

count, ma = 0, None
for i in range(N-1):
   s = data[i] + data[i+1]
   if (valid51(data[i]) + valid51(data[i+1]) == 1) \
      and s < max51:
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

