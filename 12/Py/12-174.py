# Михлин Б.С.
'''
12.174 Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды,
в обеих командах v и w обозначают цепочки цифр.
    заменить (v, w)
    нашлось (v)
Дана программа для исполнителя Редактор:
НАЧАЛО
  ПОКА нашлось (10) ИЛИ нашлось (1)
    ЕСЛИ нашлось (10)
    ТО заменить (10, 001)
    ИНАЧЕ заменить (1, 00)
    КОНЕЦ ЕСЛИ
  КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке,
состоящей из одной единицы и 75 стоящих справа от нее нулей?
В ответе запишите, сколько нулей будет в конечной строке.
'''
s = '1' + 75 * '0'
while '10' in s or '1' in s:
    # if  '10' in s:
        # s=s.replace('10','001',1)
    # else:
        # s=s.replace('1','00',1)
    s = s.replace('10', '001', 1) if '10' in s else s.replace('1', '00', 1)
print(s.count('0'))  # Ответ: 152
