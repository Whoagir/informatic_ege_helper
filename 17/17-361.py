data = [ int(x) for x in open("17-361.txt") ]

min40 = min( int(x) for x in data if abs(x) % 100 == 40 )

def findSpec( arr ):
  for i in range(3):
    if arr.count(arr[i]) == 1 and \
       arr.count(arr[(i+1)%3]) == 2:
       return i
  return -1

count = maxNo = 0
for i in range(len(data)-2):
  triple = data[i:i+3]
  specNo = findSpec( triple )
  if specNo >= 0 and all( x > min40 for x in triple ):
     count += 1
     maxNo = specNo + i + 1

print( count, maxNo )
