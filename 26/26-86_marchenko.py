
import time
time1 = time.time()
k = {}
with open("26-86.txt") as f:
    N = int(f.readline())
    for i in range(N):
        a,b = map(int, f.readline().split())
        if k.setdefault(b): # в - это Id блюда. Ключ есть
            k[b] = k[b] + [a] # добавляем в этот Id время
        else:
            k[b] = [a] # создаем новый ключ (Id = b) и заносим время [a]
for i in k.items(): # сортировка времен для каждого блюда
    k[i[0]] = sorted(i[1])
h=[] # cреднее время приготовления блюда со всеми ID
d=[0]*1000
for j, t in k.items():
    if len(t)>1:
        s=0
        k=len(t)//2
        for i in range(k):
            s+=t[2*i+1]-t[2*i]
        h.append([s/k,j])
    for i in range(1,len(t),2):
        d[t[ i ]]+=1
ss=0
for i in range(len(d)-60):
    s=sum(d[i:i+60])
    ss=max(ss,s)
print(ss,max(h)[1])
print(' время в секундах', time.time() - time1)
