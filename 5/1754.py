for n in range(1,256):
    s=bin(n)[2:]
    while len(s)<8:
        s='0'+s #достраиваем восьмибитную запись
    last=s.rfind('1')
    d=s[:last] #часть с которой выполняем преобразования
    inv=[]
    for i in d:
        if i=='0':
            inv.append('1')#инвертируем 0 на 1
        else:
            inv.append('0') #инвертируем 1 на 0
    s1=''.join(inv)+s[last::]#преобразованную часть соединяем с нетронутой
    r=int(s1,2)
    if r==221:
        print(r,n)