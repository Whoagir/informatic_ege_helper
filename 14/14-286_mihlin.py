# 14_286
# Автор: Б.С.Михлин
n0=4**2015-2**2015+15
a=1
for x in range(1,3000):
    a*=2
    n=n0+a
    k1=0
    while n:
        if n%2: k1+=1
        n//=2
    if k1==500:
        print(x) # Rez 2510 (30 c.)
        break
    
