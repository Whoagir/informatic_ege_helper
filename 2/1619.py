print('x y z f')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f=(x<=(not z)) and ((not y)<=x)
            print(int(x), int(y), int(z), int(f))