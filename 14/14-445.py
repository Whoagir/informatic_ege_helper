# Автор: П. Финкель
zz=[]
for x in range(12):
    for y in range(19):
        a=5*12**4+x*12**3+9*12*12+x*12+4
        b=7*14**3+x*14*14+x*14+6
        c=5*16**4+5*16**3+x*16*16+x*16+8
        d=3*19**3+y*19**2+x*19+7
        f=a+b+c-d
        q=[]
        for i in range(2,int(f**0.5)+1):
            if f%i==0:
                q.append(i)
                q.append(f//i)
        if len(q)==0:
            zz.append(x*y)
print(zz)
print(max(zz))
