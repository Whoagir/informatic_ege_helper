ans=[]
for n in range(4,10001):
    s='5'+'7'*n
    while '57' in s or '877' in s or '777' in s:
        if '57' in s:
            s=s.replace('57','7',1)
        if '877' in s:
            s=s.replace('877','75',1)
        if '777' in s:
            s=s.replace('777','8',1)
    sm=sum(map(int,s))
    ans.append(sm)
print(max(ans))