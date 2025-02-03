f=open('17-5.txt')
a=[int(x) for x in f]
c=0
ans=[]
for i in range(len(a)-1):
    if a[i]%2==0 or a[i+1]%2==0:
        c+=1
        ans.append(a[i]+a[i+1])
print(c,max(ans))