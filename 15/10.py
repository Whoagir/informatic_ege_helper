g=[]
for a in range(1,100):
    c=0
    for y in range(1,1001):
        for x in range(1,1001):
            f=((x<6)<=(x**2<a)) and ((y**2<=a)<=(y<=6))
            if f:
                c+=1
    if c==1000000:
        g.append(a)
print(len(g))
