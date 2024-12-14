with open('26-136.txt') as F:
  N, M = map( int, F.readline().split() )
  data = {}
  for _ in range(N):
    cost, status = map( int, F.readline().split() )
    cur = data.get( cost, [0, 0] )
    data[cost] = [ cur[0]+status, cur[1]+1-status ]

top = sorted( (x for x in data.items() if x[0] > M),
              key = lambda x: -x[1][0] )

bottom = sorted( (x for x in data.items() if x[0] <= M),
              key = lambda x: -x[1][0] )

print( top[0][0]*top[0][1][0] + bottom[0][0]*bottom[0][1][0],
       top[0][1][1] + bottom[0][1][1])





