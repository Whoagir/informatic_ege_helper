# Автор: А. Кабанов

f = open('26-76.txt')
l,n = map(int,f.readline().split())
a = [0]*l
for i in range(n):
    st, end = map(int,f.readline().split())
    a[st]+=1
    a[end]-=1

k = 0
s = 0
curr = 0
m = 0
for i in range(l):
    k+=a[i]
    if k==0:
        curr+=1
    if k>0 and curr>0:
        s += curr
        m = max(m, curr)
        curr = 0
print(s, m)


