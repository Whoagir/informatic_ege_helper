print('x y z w')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f=((z<=y) and ((not x)<=w))<=((z==w) or (y and (not x)))
                if f==0:
                    print(int(x), int(y), int(z), int(w))