f=open('17-3.txt')
a=[int (x) for x in f]
ans=0
ans1=[]
for i in range(len(a)-1):
    if (a[i]+a[i+1])%7==0 and (a[i]*a[i+1])>0:
        ans+=1
        b=a[i]*a[i+1]
        ans1.append(b)
print(ans,min(ans1))