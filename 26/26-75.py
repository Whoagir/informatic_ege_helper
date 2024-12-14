# Автор: А. Кабанов

f = open('26-75.txt')
n = int(f.readline())
a = [0]*1_000_001
for i in range(n):
    st, end = map(int,f.readline().split())
    a[st]+=1
    a[end]-=1

k = 0
m, count = 0, 0
for i in range(1_000_001):
    if k>0: count+=1
    k+=a[i]
    m = max(m,k)
print(m, count)
