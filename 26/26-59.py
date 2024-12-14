with open('26-59.txt') as F:
  N = int(F.readline())
  data = {}
  for i in range(N):
    row, seat = map( int, F.readline().split() )
    data[row] = data.get(row, []) + [seat]

for row, seats in sorted( data.items(), reverse = True ):
  seats.sort()
  done = False
  #print( row, seats )
  for i in range(len(seats)-1):
    if seats[i+1]-seats[i] == 3:
      print( row, seats[i]+1 )
      done = True
      break
  if done: break
