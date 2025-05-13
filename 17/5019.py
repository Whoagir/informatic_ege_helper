f=open('17-278.txt')
a=[int(x) for x in f]
sm7=[]
ans=[]
for k in range(len(a)):
    sm7.append((oct(a[k])).count('7'))
sm71=sum(sm7)*7
for i in range(len(a)-1):
    if int(a[i])>int(sm71) and int(a[i+1])>int(sm71):
        ans.append(a[i]+a[i+1])
print(len(ans),min(ans))
