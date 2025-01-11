def ctb(n:int, b:int)->str:
    r=''
    while n>0:
        d=str(n%b)
        r=d+r
        n//=b
    return r
s=6*1333-5*6**1215+3*6**144-86
s1=ctb(s,6)
print(s1)
one=s1.count('1')
two=s1.count('2')
three=s1.count('3')
four=s1.count('4')
five=s1.count('5')
sm=one+two*2+three*3+four*4+five*5
print(sm,s1)