with open('26-154.txt') as F:
  N = int(F.readline())
  dataNo2 = []
  dataWith2 = []
  for i in range(N):
    ID, *marks = map( int, F.readline().split() )
    ball = sum(marks) / len(marks)
    num2 = marks.count(2)
    if not num2:
      dataNo2.append( (ID, ball) )
    elif num2 > 2:
      dataWith2.append( (ID, ball, num2) )

dataNo2.sort( key = lambda x: (-x[1], x[0]) )
dataWith2.sort( key = lambda x: (x[2], x[0]) )

print( dataNo2[N//4-1][0],
       dataWith2[0][0]  )