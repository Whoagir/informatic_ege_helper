# Автор: П. Финкель
p=1
for x in range(12):
    for y in range(18):
        a=6*12**4+7*12**3+x*12*12+x*12+3
        b=2*14**3+x*14*14+9*14+x
        c=4*15**4+4*15**3+x*15*15+x*15+3
        d=2*18**3+x*18*18+y*18+7
        f=a+b+c-d
        if f>0 and f%77==0:
            p*=(x*y)
            print(x,y,f,f//77)
print(p)