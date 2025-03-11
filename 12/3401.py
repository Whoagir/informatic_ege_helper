s='7'*86
while '4444' in s or '7777' in s:
    if '4444' in s:
        s=s.replace('4444','77',1)
    else:
        s=s.replace('7777', '44',1)
print(s)