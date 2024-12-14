# PRO100-ЕГЭ
# Решение в Excel/Calc:
# https://www.youtube.com/watch?v=B_r7kOK3PJo&t=17064s

D = 6
with open("26-105.txt") as F:
  N, S = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

data.sort()
data = [ (x, (i+1)//D) for i, x in enumerate(data) ]

p = [0]*(N+1)
for i in range(1,N+1):
  p[i] = p[i-1] + data[i-1][0]

count = 0
spentSum = 0
while count < N:
  nAction = data[count][1]
  curSum = p[count+1] - (p[count+1] - p[count+1-nAction])//2
  if curSum > S: break
  count += 1          # берём товар
  #print( count, curSum )
  spentSum = curSum

print( count, S - spentSum  )
