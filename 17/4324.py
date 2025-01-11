from functions import ctb
f=open('17-4.txt')
a=[int(x) for x in f]
c=0
ans=[]
for i in range(len(a)):
    b=ctb(a[i],16)
    if b[-1]=='b' and a[i]%7==0 and a[i]%6!=0 and a[i]%13!=0 and a[i]%19!=0:
        c+=1
        ans.append(a[i])
print(c,sum(ans))