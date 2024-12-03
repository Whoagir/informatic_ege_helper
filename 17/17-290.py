data = [ int(x) for x in open("17-290.txt") ]
N = len(data)
count, ma = 0, None
for i in range(N-2):
   triple = data[i:i+3]
   if any( x % 5 == 1 for x in triple ) and \
      all( int('1000',6) <= x < int('10000',6) for x in triple ):
     count += 1
     diff = max(triple) - min(triple)
     if ma == None or diff > ma:
       ma = diff

print( count, ma )
