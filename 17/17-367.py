data = [ int(s) for s in open('17-367.txt') ]

N = len(data)
data = [10**10] + data + [10**10]

count = 0
maxLen = 0
for i in range(1,N+1):
  if any( data[i] % d == 0 for d in [data[i-1], data[i+1]] ):
    count += 1
    maxLen = max( count, maxLen )
  else:
    count = 0

print( maxLen )