# Автор: П. Финкель
p=1
for x in range(17):
    for y in range(22):
        a=5*17**4+x*17**3+x*17*17+7*17+8
        b=4*18**3+x*18*18+x*18+9
        c=8*19**4+8*19**3+x*19*19+x*19+5
        d=6*22**4+x*22**3+y*22**2+2*22+3
        f=a+b+c-d
        if f>0 and f%405==0:
            p*=(x*y)
            print(x,y,f,f//405)
print(p)