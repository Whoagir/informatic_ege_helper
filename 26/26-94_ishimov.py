# Автор: М. Ишимов

f = open('26-94.txt')
n, k = map(int, f.readline().split())
a1 = [[] for x in range(100001)]
a2 = [[] for x in range(100001)]
ans = []

for i in range(n):
    e, r, m = map(int, f.readline().split())
    if e == 1:
        a1[r].append(m)
    elif e == 2:
        a2[r].append(m)

for r in range(100001):
  if a1[r]:
    a1[r].sort()
    if a1[r][0] >= 5 or k - a1[r][-1] >= 4:
      ans.append( (1, r) )
  if a2[r]:
    a2[r].sort()
    if a2[r][0] >= 5 or k - a2[r][-1] >= 4:
      ans.append( (2, r) )


print( max(ans, key=lambda x: x[1])[1], len(ans) )