for x1 in range(11):
    for x2 in range(11):
        x3=str(x1) if x1<10 else ''
        x4=str(x2) if x2<10 else ''
        x5=x3+x4
        for x6 in range(11):
            for x7 in range(11):
                x8=str(x6) if x6<10 else''
                x9=str(x7) if x7<10 else ''
                x10=x8+x9
                s='12'+str(x5)+'45'+str(x10)
                # print(s)
                s1=int(s)
                if s1<10**6 and s1%51==0:
                    print(s1,s1//51)