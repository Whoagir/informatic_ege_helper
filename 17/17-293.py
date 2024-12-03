data = [ int(x) for x in open("17-292.txt") ]
N = len(data)
count, mi = 0, None
for i in range(N-1):
   pair = data[i:i+2]
   if abs(pair[0] % 17 - pair[1] % 17) ==  pair[0] % 4 + pair[1] % 4:
     count += 1
     s = sum(pair)
     if mi == None or s < mi:
       mi = s

print( count, mi )
