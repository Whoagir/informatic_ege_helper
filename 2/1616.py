print('x y z f')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f=(x<=y) and (y<=z)
            print(int(x), int(y), int (z), int (f))