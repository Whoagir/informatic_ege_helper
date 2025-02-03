a=[]
for n in range(1,1000):
    s=bin(n)[2:]
    v=s.find('1')
    s1=s[v+1:]
    if s1.count('1')%2==0:
        s2='10'+s1
    else:
        s2='1'+s1+'0'
    r=int(s2,2)
    if r<450:
        a.append(r)
print(max(a))