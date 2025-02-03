for a in range(1,50):
    for b in range(1,50):
        for c in range(1,50):
            s='0'+c*'3'+b*'2'+a*'1'+'0'
            while '00' not in s:
                s=s.replace('01','210',1)
                s=s.replace('02','3101',1)
                s=s.replace('03','2012',1)
            if s.count('1')==56 and s.count('2')==44 and s.count('3')==19:
                print(a+b+c+2)