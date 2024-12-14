with open('26-84.txt') as F:
   N = int(F.readline())
   groups = sorted( [ int(x) for x in F.readline().split() ] )
   rooms = sorted( [ int(x) for x in F.readline().split() ] )

counts = [0] * N
iGroup = 0
for i, r in enumerate(rooms):
  while iGroup < N and groups[iGroup] <= r:
    iGroup += 1
  counts[i] = iGroup

variants = 1
for i in range(N):
  variants = variants * (counts[i] - i) % 100000007

print( variants, counts[0] )