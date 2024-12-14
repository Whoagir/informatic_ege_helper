with open("26-134.txt") as F:
  N, T = map( int, F.readline().split() )
  queueG, queueW, queueM = [], [], []
  for _ in range(N):
    t0, dt, cat = F.readline().split()
    if cat == 'G':
      queueG.append( (int(t0), int(dt), cat) )
    elif cat == 'W':
      queueW.append( (int(t0), int(dt), cat) )
    else:
      queueM.append( (int(t0), int(dt), cat) )

queueG.sort()
queueW.sort()
queueM.sort()

def nextPerson( t ):
  person = None
  if queueG and queueG[0][0] <= t:
    person = queueG.pop(0)
  elif queueW and queueW[0][0] <= t:
    person = queueW.pop(0)
  elif queueM and queueM[0][0] <= t:
    person = queueM.pop(0)
  return person

t = 1
count = {}
while t < T:
  cur = nextPerson( t )
  if cur:
    t0, dt, cat = cur
    print( t, t0, dt, cat )
    count[cat] = count.get(cat, 0) + 1
    t = t + dt
  else:
    if not (queueG or queueW or queueM):
       break
    t += 1

print( sum(count.values()), count[cat] )
