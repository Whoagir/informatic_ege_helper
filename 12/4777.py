for n in range(400,1000):
    s='5'*n
    while '5555' in s:
        s=s.replace('5555','8',1)
        s=s.replace('88','5',1)
    v=s.count('5')
    print(v, n)
