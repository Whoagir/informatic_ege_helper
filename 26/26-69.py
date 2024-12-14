# Автор: А. Кабанов
# Разбор: https://youtu.be/DqXIo7pHk3A

f = open('26-69.txt')
n = int(f.readline())
a = [list(map(int,f.readline().split())) for i in range(n)]
a.sort(key=lambda x:(-x[0],x[1]))

m = curr = 1
r = 0
for i in range(n-1):
    if a[i+1][0] == a[i][0] and a[i+1][1] == a[i][1] + 1:
        curr += 1
        if curr > m:
            m, r = curr, a[i][0]
    else:
        curr = 1
print(r,m)


