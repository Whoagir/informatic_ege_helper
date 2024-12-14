with open('26-66.txt') as f:
  N, START = map(int, f.readline().split())
  END = START + 24*3600*1000
  data = []
  for i in range(N):
    t0, t1 = map(int, f.readline().split())
    if t1 == 0: t1 = 10**10
    data.extend( [t0, -t1] )

data.extend( [-START, START] ) # учесть первый интервал
data.append( -END )            # учесть последний интервал
data.sort( key = abs )

nProc = maxProc = 0
maxTime = 0
prev = 0
for i, t in enumerate(data):
   nProc += 1 if t >= 0 else -1
   if START <= abs(t) <= END:
     if nProc > maxProc:
        maxProc, maxTime = nProc, 0
     else:
        if prev == maxProc:
          maxTime += abs(t) - abs(data[i-1])
          # print( t, maxProc, maxTime, abs(t) - abs(data[i-1]) )
     prev = nProc

print( maxProc, maxTime )

