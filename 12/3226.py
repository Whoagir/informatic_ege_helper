c=1000
for n in range(51,1000):
    s='1'*n
    while '111' in s:
        s=s.replace('111','22',1)
        s=s.replace('222','11',1)
    v=s.count('1')
    print(v,n)
