# Автор: А. Кабанов

f = open('26-77.txt')
n = int(f.readline())
a = [[0]*9 for i in range(31)]
for i in range(n):
    x,y = map(int, f.readline().split())
    a[x][y] = 1

count = 0
m = 0
mi = 0
for i in range(1,31):
    remain = 8 - sum(a[i])
    count+= remain
    if remain >= m:
        m = remain
        mi = i
print(count, mi)
