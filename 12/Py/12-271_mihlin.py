# Михлин Б.С.
'''
12.271 (А. Богданов) Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды,
в обеих командах v и w обозначают цепочки символов. 
    заменить (v, w) 
    нашлось (v) 
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет,
эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор. 
Дана программа для Редактора:
ПОКА нашлось(43) ИЛИ нашлось(53)
  ЕСЛИ нашлось(43)
    ТО заменить(43, 33)
    ИНАЧЕ заменить(53, 433)
КОНЕЦ ПОКА
Определите максимально возможное количество цифр 3, которое может получиться в результате применения этой программы к строке,
состоящей из 17 цифр 3, 23 цифр 4 и 29 цифр 5, идущих в произвольном порядке.
'''
# s = 17 * '3' + 23 * '4' + 29 * '5'  # Так нельзя! Надо, чтобы '3' стояла справа от '5' и '4'
# Несколько вариантов исходной строки s, дающих максимальное количество цифр '3':
s = 23 * '4' + 29 * '5' + 17 * '3'
# s = 16 * '3' + 23 * '4' + 29 * '5' + '3'
# s = 29 * '5' + 23 * '4' + 17 * '3'

while '43' in s or '53' in s:
    s = s.replace('43', '33', 1) if '43' in s else s.replace('53', '433', 1)
print(s.count('3'))  # Ответ: 98
