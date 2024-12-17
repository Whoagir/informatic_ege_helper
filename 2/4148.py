print ('a b c d')
x=[True,False]
for a in x:
    for b in x:
        for c in x:
            for d in x:
                f=((a and b)==(not c)) and (b<=d)
                if f==1:
                    print(int(a), int(b), int(c),int(d))