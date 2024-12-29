print('x y z')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f=(y<=z) and (not(z and x))
            if f==1:
                print(int(x), int(y),int(z))