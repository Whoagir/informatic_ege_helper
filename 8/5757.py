from itertools import *
a='АНТИУОПЯ'
alg='АИУОЯ'
als='НТП'
comb=product(a,repeat=6)
c=0
for i in comb:
    s=''.join(i)
    for k in range(0,7):
        s1=s[:k]
        s2=s[k:]
    # print(s,s1,s2)
        s3=''
        s4=''
        s5=''
        s6=''
        for j in s1:
            if j in alg:
                s3+=j
            else:
                s4+=j
        for j in s2:
            if j in alg:
                s5+=j
            else:
                s6+=j
        # print(s,s3,s4,s5,s6,'             ', sorted(s3),s3==sorted(s3))
        if s3==''.join(sorted(s3)) and s4[::-1]==''.join(sorted(s4)):
            if s5[::-1]==''.join(sorted(s5)) and s6==''.join(sorted(s6)):
                # print(s,s1,s2)
                c+=1
print(c)
