for n in range(100,120):
    s='1'*n
    while '111' in s:
        s.replace('111','2',1)
        s.replace('2222','333',1)
        s.replace('33','1',1)
        print(s,n)