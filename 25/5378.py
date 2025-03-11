for m in range(0,10):
    for n1 in range(0,11):
        for n2 in range(0,11):
            n3=str(n1) if n1<10 else ''
            n4=str(n2) if n2<10 else ''
            n=n3+n4
            s='12'+str(n)+'4'+str(m)+'65'
            if int(s)%161==0:
                print(s,int(s)/161)