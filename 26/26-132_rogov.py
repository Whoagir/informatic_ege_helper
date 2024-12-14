# Автор: А. Рогов

f = open('26-132.txt')
n, k = map(int, f.readline().split())
a = [[int(j) for j in i.split()] for i in f][:n]

a.sort()

# Идея решения: моделирование ситуации. В каждую секунду происходит ряд процессов:
# 1. Освобождаются те операторы, которые закончили обслуживание
# 2. Пришедшие посетители встают в очередь, если она есть.
# 3. Прием операторами из очереди

q = [] # очередь
oper = [0] * k # операторы. Хранится время, когда освободится
last = 0 # последний оператор, принявший посетителя
count = 0 # общее количество принятых посетителей
prevOper = oper[:]
prevQueue = []
for t in range(86400):
  # освобождение
  for i in range(k):
    if oper[i] == t:
      oper[i] = 0
  # уходят из очереди
  while t in q:
    q.remove(t)
  # прием из очереди
  while 0 in oper and q:
    last = oper.index(0)
    count += 1
    oper[oper.index(0)] = q.pop(0)
  # занимаем
  for st, fn in a:
    if st == t:
      # есть пришедший
      if 0 in oper:
        # принимают сразу
        last = oper.index(0)
        count += 1
        oper[oper.index(0)] = fn
      else:
        # встает в очередь
        q.append(fn)

"""
  if oper != prevOper or q != prevQueue:
    print( t )
    print( 'Ops:', oper )
    print( 'Queue:', q )
    print( 'Count:', count )

  prevOper = oper[:]
  prevQueue = q[:]
"""

print(count, last + 1)