print('x y z w')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f=(((y<=x) or ((not z) and w))==(w==x))
                if f==1:
                    print(int(x), int (y), int(z), int(w))