print('x y z')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f=(z or y)<=(x==z)
            if f==0:
                print(int(x), int(y), int(z))