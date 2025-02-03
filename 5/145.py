for n in range(999,101,-1):
    j=str(n)
    s=int(j[0])*int(j[1])
    s2=int(j[1])*int(j[2])
    if s>s2:
        s3=str(s2)+str(s)
    else:
        s3=str(s)+str(s2)
    if s3=='621':
        print(n,s3)
        break