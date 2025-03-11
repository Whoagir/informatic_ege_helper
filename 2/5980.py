print('x y z w f')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f=(x==(z<=y)) and (not w)
                print(int(x), int(y), int(z), int(w), int(f))