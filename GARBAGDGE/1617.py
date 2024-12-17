print('x y z')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f=(x<=y) and (y<=z)
            if f==1:
                print (int(x), int(y),int(z))