for x in range(14,0,-1):
    s=int('1'+str(x)+'51',15)-int('3'+str(x)+'2',15)
    if s%4==0:
        print(s//4)
