# 14_291
#Автор: Б.С.Михлин
n0=125**7-25**4
for x in range(1,1000):
    n=n0+x
    k4,k3,k1=0,0,0
    while n:
        d=n%5
        if d==4:
            k4+=1
        elif d==3:
            k3+=1
        elif d==1:
            k1+=1
        n//=5
    if k4==15 and k3==1 and k1==2:
        print(x) # Rez 849
        break
    
