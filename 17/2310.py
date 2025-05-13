f=open('17_2310.txt')
a=[int(x) for x in f]
ans=[]
mn=268
mx=9840
sm=mn+mx
for i in range(len(a)-1):
    if a[i]+a[i+1]<sm:
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))