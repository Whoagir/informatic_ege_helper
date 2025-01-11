f=open('17-377.txt')
a=[int(x) for x in f ]
mx=[]
ans=[]
c=0
for i in range(len(a)-1):
    if i%17==0:
        mx.append(i)
mx1=max(mx)
for i in range(len(a)-1):
    b=a[i]+a[i+1]
    if b>mx1:
        c+=1
        ans.append(b)
print(c,max(ans))