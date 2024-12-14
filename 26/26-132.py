with open('26-132.txt') as F:
  N, K = map(int, F.readline().split())
  data = []
  for i in range(N):
    tStart, tEnd = map(int, F.readline().split())
    data.extend( [ (tStart, tEnd, i+1), (-tEnd, tEnd, i+1) ] )

data.sort( key = lambda x: (abs(x[0]), x[0]) )

queue = []
operators = [0]*K
lastOper = 0
count = 0
for t, tEnd, i in data:
   #print( '>', t, tEnd, i )
   if t < 0:
     for tq, te, iq in queue[:]:
       if te <= abs(t):
         queue.remove( (tq, te, iq) )
     for j in range(K):
       if operators[j] == i:
         operators[j] = 0
         if queue:
           tq, te, iq = queue.pop(0)
           operators[j] = iq
           last, count = j, count+1
         break
   else:
     for j in range(K):
       if operators[j] == 0:
         operators[j] = i
         last, count = j, count + 1
         break
     else:
       queue.append( (t, tEnd, i) )
   #print( 'Ops:', operators )
   #print( 'Queue:', queue )
   #print( 'Count:', count )

print( count, last+1 )