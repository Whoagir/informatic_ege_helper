for x in range(0,10):
    for y1 in range(0,11):
        for y2 in  range(0,11):
            for y3 in range(0,11):
                y11=str(y1) if y1<10 else''
                y21 = str(y2) if y2 < 10 else ''
                y31 = str(y3) if y3 < 10 else ''
                y=y11+y21+y31
                s='3'+str(x)+'1'+str(y)+'57'
                if int(s)%2023==0:
                    print(s,int(s)//2023)