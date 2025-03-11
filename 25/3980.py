for m in range(1,34,2):
    for n in range(0,34,2):
        s=(2**m)*(5**n)
        if 10**8<s<3*10**8:
            print(s,m+n)