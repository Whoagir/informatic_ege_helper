# Автор: Б.С. Михлин
# 12.281

m=set()
for n in range(2,1001):
    s=n*'5'
    while '555' in s or '888' in s:
        s=s.replace('555','8',1)
        s=s.replace('888','55',1)
    m.add(s)
print(len(m),m)
# Rez
'''
7 {'85', '88', '855', '55', '885', '8', '8855'}
'''
