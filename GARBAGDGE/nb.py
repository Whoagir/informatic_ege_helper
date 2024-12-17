def ctb(number,base):
    s=''
    while number>0:
        s=s+str(number%base)
        number=number//base
    return s[::-1]
b=(7**(9**2-1)-(10-3)**4)*5/6*8
m=ctb(b,7)
m1=m.count('4')
print(m1)