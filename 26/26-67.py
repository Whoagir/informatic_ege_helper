with open('26-66.txt') as f:
  N, START = map(int, f.readline().split())
  END = START + 24*3600*1000
  #print( START, END-1 )
  data = []
  for i in range(N):
    t0, t1 = map(int, f.readline().split())
    if t1 == 0: t1 = 10**10
    data.extend( [t0, -t1] )

data.extend( [START, -START] ) # учесть первый интервал
data.append( END )             # учесть последний интервал
data.sort( key = abs )

nProc = 0
allChunks = []
for i, t in enumerate(data):
   nProc += 1 if t >= 0 else -1
   if START <= abs(t) <= END:
     if allChunks and allChunks[-1][1] == abs(t):
        allChunks.pop()
     allChunks.append( (nProc, abs(t)) )

minProc, maxTime = 10**10, 0
for i in range(len(allChunks)-1):
   nProc, t = allChunks[i]
   if nProc < minProc:
      minProc = nProc
      maxTime = 0
   if nProc == minProc:
      maxTime += allChunks[i+1][1] - t

print( minProc, maxTime )

"""
nProc, minProc = 0, 10**10
maxTime = 0
prev = 0
for i, t in enumerate(data):
   nProc += 1 if t >= 0 else -1
   print( abs(t), nProc )
   if START <= abs(t) <= END:
     if nProc < minProc:
        minProc, maxTime = nProc, 0
     else:
        if prev == minProc:
          maxTime += abs(t) - abs(data[i-1])
          print( t, minProc, maxTime, abs(t) - abs(data[i-1]) )
     prev = nProc

print( minProc, maxTime )
"""