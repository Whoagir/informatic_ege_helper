# Автор: Информатик-БУ

f = open('26-111.txt')
k = int(f.readline())
n = int(f.readline())
a = sorted( list(map(int, f.readline().split())) for _ in range(n) )
f.close()

count = 0
lastStart, xLast = 0, -1
for x in range(k):
  t = [a[0]]
  if t[-1][0] > lastStart:
    lastStart, xLast = t[-1][0], x
  a.pop(0)
  for j in range(10):
    mn = [100500, 0]
    dl = -1
    for i in range(len(a)):
      if a[i][0] > t[-1][1]:
        mn = a[i]
        dl = i
        break
    if dl == -1: break
    t.append( mn )
    if t[-1][0] > lastStart:
      lastStart, xLast = t[-1][0], x
    a.pop( dl )
  #print( x+1, t )
  count += len(t)

print( count, xLast + 1 )