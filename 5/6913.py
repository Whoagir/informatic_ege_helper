c=0
for n in range(10000,100000):
    s=oct(n)[2:]
    print(s)
    s=s.replace('1','2').replace('3','2').replace('5','2').replace('7','2')
    print(s)
    s1=s+str(n%8)
    r=int(s1,8)
    s2 = oct(r)[2:]
    s2 = s2.replace('1', '2').replace('3','2').replace('5','2').replace('7','2')
    s3 = s2 + str(r % 8)
    r1 = int(s3, 8)
    if r1%2023==0:
        c+=n
print(c)