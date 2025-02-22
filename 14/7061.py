for x in range(3,51):
    s=int('7'+str(x)+'5893',17)+int('ee'+str(x)+'39ac',17)
    if s%13==0:
        print(s/13)
        break