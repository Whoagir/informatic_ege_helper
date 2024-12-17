for n in range(101,200):
    s='8'*n
    while ('555' in s) or ('888' in s):
        s=s.replace('555','8',1)
        s=s.replace('888','55',1)
    if s.count('8')==0:
        print(n)
        break