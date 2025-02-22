for n in range (1,1000):
    s=bin(n)[2:]
    if n%2==0:
        s1=s+'01'
    else:
        s1=s+'10'
    r=int(s1,2)
    if r>138:
        print(n)
        break