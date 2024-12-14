with open('26-61.txt') as F:
  N, M = map( int, F.readline().split() )
  photo = []
  video = []
  for i in range(N):
    v = int(F.readline())
    if v <= 100:
          photo.append(v)
    else: video.append(v)

photo.sort( reverse = True )
video.sort()

count = 0
vVideo = 0
i = 0
while vVideo < M / 2:
  vVideo += video[i]
  count += 1
  i += 1
M -= vVideo

i = 0
while M > photo[-1]:
  last = photo.pop()
  M -= last
  count += 1
  i += 1

photo.append( last )
best = max( ph for ph in photo if ph <= M + last )

print( count, best )










