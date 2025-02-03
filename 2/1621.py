print('x y z')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f=((not x) or z) and ((not x) or (not y) or (not z))
            if f==0:
                print(int(x), int (y), int (z))