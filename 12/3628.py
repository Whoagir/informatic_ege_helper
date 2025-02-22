s='AB'*52
while 'AA' in s or 'BB' in s or 'AB' in s:
    s=s.replace('AA','B',1)
    s=s.replace('BB','A',1)
    s=s.replace('AB','BA',1)
print(s)