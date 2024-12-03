data = [ int(x) for x in open("17-292.txt") ]
N = len(data)
count, ma = 0, None
for i in range(N-1):
   pair = data[i:i+2]
   if pair[0] % 6 + pair[1] % 6 ==  pair[0] % 11 + pair[1] % 11:
     count += 1
     s = sum(pair)
     if ma == None or s > ma:
       ma = s

print( count, ma )
