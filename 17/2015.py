f=open('17_2015.txt')
a=[int(x) for x in f]
ans=[]
for i in range(len(a)):
    if (str(a[i])[-1]=='5' or str(a[i])[-1]=='7') and a[i]%9!=0 and a[i]%11!=0:
        ans.append(a[i])
mx=max(ans)
mn=min(ans)
ans1=mx+mn
print(len(ans),ans1)