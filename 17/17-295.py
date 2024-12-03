data = [ int(x) for x in open("17-295.txt") ]

def prodDigits( n ):
  p = 1
  for x in map(int, str(n)):
    p *= x
  return p

N = len(data)
M = max(data)

count, ma = 0, None
for i in range(N-1):
   pair = data[i:i+2]
   s = sum(pair)
   pDigits = prodDigits(s)
   if pDigits != 0 and s % pDigits == 0 and s < M:
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )
