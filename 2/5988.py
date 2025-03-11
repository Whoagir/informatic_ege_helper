print('x y z w f')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f=w and ((z or y)==(z and x))
                print(int(x), int(y), int(z), int(w), int(f))