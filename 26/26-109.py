# PRO100 ЕГЭ

with open('26-109.txt') as F:
  N = int( F.readline() )
  data = [ int(s) for s in F ]

data.sort()
data = [0] + data
s = [0]*(N+1)
for i in range(1,N+1):
  s[i] = s[i-1] + data[i]

D = 6
S = 100000
for i in range(N):
  nDiscount = i // 6
  nFullPrice = i - nDiscount
  cost = s[nFullPrice] + 0.5*(s[i] - s[nFullPrice])
  if cost > S: break
  diff = S - cost
  count = i

print( count, int(diff) )


