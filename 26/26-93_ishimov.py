# Автор: М. Ишимов

f = open('26-93.txt')
n, m = map(int, f.readline().split())
a = [[0] * 5001 for x in range(2001)]
ans = []

for i in range(n):
    floor, place = map(int, f.readline().split())
    a[floor][place] += 1

for floor in range(1, 2001):
    s = [0]
    count = 0
    for p in range(1, 5001):
        if a[floor][p] == 0: s.append(0)
        elif a[floor][p-1] == 0 or p == 1: s.append(1)
        else: s[-1] += 1
    s += [0]
    for p in range(1, len(s) - 1):
      x,y,z = s[p-1], s[p], s[p+1]
      if y == 0 and x+z >= m:
        count += 1
        ans.append(floor)

print(len(ans), max(ans))