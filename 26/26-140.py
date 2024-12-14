with open('26-140.txt') as F:
  N = int(F.readline())
  data = []
  for i in range(N):
    t0, t1 = map( int, F.readline().split() )
    data.append( (t0, t1) )

busy = [' ']*44641
for t0, t1 in data:
  for t in range(t0, t1):
    busy[t] = '1'
s = ''.join(busy)
print( s.count('1') )
print( len( max(s.split(), key = len) ))
