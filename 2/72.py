print('a b c f')
x=[True,False]
for a in x:
    for b in x:
        for c in x:
            f=(not a) or (b and (not c))
            print(int(a), int(b), int(c),int(f))