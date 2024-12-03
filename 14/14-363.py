# Автор И. Степанов

def perevod(s,c,x):
    a = 0
    for i in range(len(s)):
        if s[i] != 'x':
            a += int(s[i],36) * c**i
        else:
            a+= x * c**i
    return a

dig =[i for i in range(44)]
for x in dig:
    s1='1x23'[::-1]
    s2='32x1'[::-1]
    res = perevod(s1,44,x) + perevod(s2,44,x)
    if res % 42 == 0:
        print('x =', x)
        rs = res
print('Otvet:', rs/42)

# x = 41 Ответ: 10140
