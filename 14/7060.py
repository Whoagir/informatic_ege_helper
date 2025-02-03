for x in range(15,-1,-1):
    s=int('3bb'+str(x)+'8',16)+int('b67a'+str(x)+'fe62',16)+int('bea2'+str(x)+'d49b',16)+int('8d7d'+str(x),16)
    if s%15==0:
        print(s/15)