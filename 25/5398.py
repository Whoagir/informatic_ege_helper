ans=[]
for m in range(0,10):
    for n1 in range(0,11):
        for n2 in range(0,11):
            for n3 in range(0,11):
                n4=str(n1) if n1<10 else ''
                n5=str(n2) if n2<10 else ''
                n6=str(n3) if n3<10 else ''
                n=n4+n5+n6
                s='12345'+str(n)+'76'
                if int(s)%73==0:
                    ans.append(int(s))
ans=list(set(ans))
ans=sorted(ans)
print(ans)
for i in ans:
    print(int(i), int(i)//73)