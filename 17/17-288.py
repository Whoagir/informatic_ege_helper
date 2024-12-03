data = [ int(x) for x in open("17-288.txt") ]
N = len(data)
count, mi = 0, None
for i in range(N-2):
   triple = data[i:i+3]
   if len(set(abs(x) % 7 for x in triple)) == 3 and \
     any( x < 0 for x in triple ):
     count += 1
     diff = max(triple) - min(triple)
     if mi == None or diff < mi:
       mi = diff

print( count, mi )
