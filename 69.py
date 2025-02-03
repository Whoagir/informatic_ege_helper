print('a b c f')
x=[True,False]
for a in x:
    for b in x:
        for c in x:
            f=(a and (not c)) or ((not b) and (not c))
            print(int(a), int(b), int (c), int(f))