from functions import pr
for n in range(61,70):
    s='0'+'1'*n+'2'*80+'0'
    while '00' not in s:
        s=s.replace('02','101',1)
        s = s.replace('11', '2', 1)
        s = s.replace('012', '30', 1)
        s = s.replace('010' , '00', 1)
    sm=sum(map(int,str(s)))
    if pr(sm)==True:
        print(n)
        break