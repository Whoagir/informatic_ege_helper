s='3'*17+'4'*23+'5'*29
while '43' in s or '53' in s:
    if '43' in s:
        s=s.replace('43','33',1)
    else:
        s=s.replace('53','433',1)
c=s.count('3')
print(c)