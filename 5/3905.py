for n in range(91,1000):
    s=bin(n)[2:]
    if s.count('1')==s.count('0'):
        s1=s+s[-1]
    elif s.count('1')>s.count('0'):
        s1=s+'0'
    elif s.count('1')<s.count('0'):
        s1=s+'1'
    if s1.count('1') == s1.count('0'):
        s2 = s1 + s1[-1]
    elif s1.count('1') > s1.count('0'):
        s2 = s1 + '0'
    elif s1.count('1') < s1.count('0'):
        s2 = s1 + '1'
    if s2.count('1')==s2.count('0'):
        s3=s2+s2[-1]
    elif s2.count('1')>s2.count('0'):
        s3=s2+'0'
    elif s2.count('1')<s2.count('0'):
        s3=s2+'1'
    print(s,s1,s2,s3)
    r=int(s3,2)
    if r%2==0 and r%4!=0:
        print(n)
        break
