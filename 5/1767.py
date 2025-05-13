for n in range(1,1000):
    s=bin(n)[2:]
    s1=s[::-1]
    r=int(s1,2)
    if r==15:
        if n>500:
            print(n)