def pr(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True
ans=[]
for x in range(0,10):
    for x1 in range(0,10):
        for x2 in range(0,10):
            for y in range(0,11):
                y1=str(y) if y<10 else ''
                s='12'+str(x)+'5'+str(y)+'5'+str(x1)+str(x2)
                s1=int(s)
                if s1%311==0:
                    c=s1//311
                else:
                    continue
                if pr(c):
                    print(s1,c)