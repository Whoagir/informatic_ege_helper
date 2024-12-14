# Автор: А. Кабанов

f = open('26-150.txt')
N, M, K = [int(x) for x in f.readline().split()]
min_ryad = [M+1]*(K+1)

for i in range(N):
  r, m = [int(x) for x in f.readline().split()]
  min_ryad[m] = min(min_ryad[m], r)

ans1 = 0
for i in range(1,K):
  ans1 = max(ans1, min(min_ryad[i]-1, min_ryad[i+1]-1))

ans2 = []
for i in range(1,K):
  if min(min_ryad[i]-1, min_ryad[i+1]-1) == ans1:
    ans2.append( i+1 )

print( ans1, max(ans2) )