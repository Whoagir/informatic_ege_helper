# Автор: А. Козлов

for n in range(1,240):
    kk = s = bin(n)[2:]
    if s.count("1")%2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    if int(s,2)>40:
        # print(n,kk,s,int(s,2)) данная строка для визуализации работы программы
        break
print('ответ:',n)