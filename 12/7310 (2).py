d=10000
for a in range(0,50):
    for b in range(0,50):
        for c in range(0,50):
            s='0'+'1'*a+'2'*b+'3'*c+'0'
            s1=s
            while '00' not in s:
                s=s.replace('01','2320',1)
                s=s.replace('02','1013',1)
                s=s.replace('03','12    10',1)
            if s.count('1')==36 and s.count('2')==30:
                if d>len(s1):
                    d=len(s1)
print(d)