for n in range(1, 256):
    s = bin(n)[2:]
    #print(s)
    while len(s)<8:
        s='0'+s
    #print(s)
    s1=''
    for j in s:
        s1=s1+str(1-int(j))
    r=int(s1,2)
    if r==11:
        print(n)