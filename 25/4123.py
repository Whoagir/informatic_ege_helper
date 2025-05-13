ans=[]
ans1=[]
for a in range(1,5001):
    for b in range(a,5001):
        t2=a**2+b**2
        c=int(t2**0.5)
        if c**2==t2 and c<=5000:

            ans.append(c+a+b)
            if a+b+c==12040:
                print(c)
print(len(ans))