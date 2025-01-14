print('x y z')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f= ((not x) and z) or ((not x) and (not y) and (not z))
            if f==1:
                print( int(x), int(y), int(z))