print('a b c d')
x=[True,False]
for a in x:
    for b in x:
        for c in x:
            for d in x:
                f=(a<=b)and(c<=d)or(not c)
                if f==0:
                    print(int(a), int(b), int(c), int (d))