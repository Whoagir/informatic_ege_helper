f=open('17-5.txt')
a=[int(x) for x in f]
c=0
ans=[]
for i in range (len(a)-1):
    if str(a[i])[-1]=='5' and str(a[i+1])[-1]=='5':
        c+=1
        v=a[i]+a[i+1]
        ans.append(v)
print(c,max(ans))