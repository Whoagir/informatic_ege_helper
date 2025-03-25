f=open('17_2016.txt')
a=[int(x) for x in f]
ans=[]
for i in range(len(a)):
    if a[i]%13==7 and a[i]%7!=0 and a[i]%11!=0:
        ans.append(a[i])
mx=max(ans)
mn=min(ans)
ans1=mx-mn
print(len(ans),ans1)