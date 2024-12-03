# Автор И. Степанов

def perevod(s,c,x):
    a = 0
    for i in range(len(s)):
        if s[i] != 'a':
            a += int(s[i],36) * c**i
        else:
            a+= x * c**i
    return a

dig =[i for i in range(55)]
b = 29
otv = []
for a in dig:
    s1='ZaYX'[::-1]
    s2='2XaY'[::-1]
    res = perevod(s1,55,a) - perevod(s2,55,a)
    if res % b == 0:
        print(a, res, 'Частное:', res/b)
        otv.append(res)
print('Otvet:', max(otv)-min(otv))

# a = 23, 52
# Ответ: 86130

