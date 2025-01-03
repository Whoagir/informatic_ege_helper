# Михлин Б.С.
'''
13.23 На месте преступления были обнаружены пять обрывков бумаги.
Следствие установило, что на них записаны фрагменты одного IP-адреса.
Криминалисты обозначили эти фрагменты буквами А, Б, В, Г и Д.
Восстановите IP-адрес. В ответе укажите последовательность букв, обозначающих фрагменты,
в порядке, соответствующем IP-адресу. Известно, что последнее число было трехзначным
'''
from itertools import *
ip = '.65 10 39 4.28 .2'.split()  # ip - список с обрывками IP-адреса
for IP in map(''.join, permutations(ip)):
    x = IP.split('.')  # x - список из частей IP-адреса нарезанных по точкам
    for p in x:        # p (part) - часть IP-адреса
        if p == '' or int(p) > 255:
            break
    else:
        print('IP-адрес:', IP)
# IP-адрес: 104.28.65.239 Подходит. Следовательно, ответ: БГАДВ
# IP-адрес: 104.28.239.65 Не подходит.
