# Автор: Н.Т. Гаязова

f=open("26-53.txt")
a=set()
b=[]
n=int(f.readline())
for i in range(n):
    x=int(f.readline())
    a.add(x)
    if x%2==1: b.append(x)

c=set()
for i in range(0,len(b)-1):
    for j in range(i+1,len(b)):
        c.add((b[i]+b[j])/2)
w=a&c
print(len(w),max(w))
