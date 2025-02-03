print('x y z w')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f=((x and w) or (w and z))==((z<=y) and (y<=x))
                if f==1:
                    print(int(x), int(y), int(z), int(w))