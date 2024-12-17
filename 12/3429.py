s='5'*200
while '555' in s or '333' in s:
    if '555' in s:
        s=s.replace('555','3',1)
    else:
        s=s.replace('333','5',1)
c=s.count('5')*5+s.count('3')*3
print(s)
print(c)