from functions import ctb
f=open('17-4.txt')
a=[int(x) for x in f]
ans=[]
for i in range(len(a)):
    b=hex(a[i])[2:]
    if b[-1]=='b' and a[i]%7==0 and a[i]%6!=0 and a[i]%13!=0 and a[i]%19!=0:
        ans.append(a[i])
print(len(ans),sum(ans))