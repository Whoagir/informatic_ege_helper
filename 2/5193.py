print('x y z w')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f=(y or x)==(y<=w)or (not z)
                if f==0:
                    print(int(x), int(y), int(z), int(w))