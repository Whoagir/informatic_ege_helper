data = [ int(x) for x in open("17-296.txt") ]

sumFirst = sum( int(str(abs(x))[0]) for x in data )

N = len(data)

count, ma = 0, None
for i in range(N-1):
   if data[i]*data[i+1] > sumFirst:
     count += 1
     s = data[i] + data[i+1]
     if ma == None or s > ma:
       ma = s

print( count, ma )
