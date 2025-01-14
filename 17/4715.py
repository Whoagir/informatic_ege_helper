f=open('17-243.txt')
a=[int(x) for x in f]
kr=[]
ans=[]
c=0
for i in  range (len(a)-1):
    if a[i]%33==0:
        kr.append(a[i])
v=sum(kr)
for i in range(len(a)-1):
    if a[i]>v or a[i+1]>v:
        c+=1
        ans.append(a[i]+a[i+1])
print(c)