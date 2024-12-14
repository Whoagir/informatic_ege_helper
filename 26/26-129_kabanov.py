# Автор: А. Кабанов

f = open('26-129.txt')
n = int(f.readline())
details = []
for i in range(n):
  shl, okr  = map(int, f.readline().split())
  if shl < okr: # все числа различны
    details.append( [shl, 'shl', i+1] )
  else:
    details.append( [okr, 'okr', i+1] )

details.sort()

lenta = [0]*n
last = 0
kshl = last_shl = 0
for i in range(n):
  t, tp, num = details[i]
  if tp == 'shl':
    for j in range(n):
      if lenta[j] == 0:
        lenta[j] = 1
        last = num
        last_shl = kshl
        kshl += 1
        break
  else:
    for j in reversed(range(n)):
      if lenta[j] == 0:
        lenta[j] = 1
        last = num
        last_shl = kshl
        break

print( last, last_shl )

