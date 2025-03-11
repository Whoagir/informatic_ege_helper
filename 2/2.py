print('x y z f')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f=(not z) and x or x and y
            print(int(x), int(y), int(z), int(f))