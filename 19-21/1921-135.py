# Михлин Б.С.
'''
1921.135 (А. Минак) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней.
Игроки ходят по очереди, первый ход делает Петя.
За один ход игрок может добавить в кучу один камень либо увеличить количество камней в куче в два раза.
    Например, имея кучу из 10 камней, за один ход можно получить кучу из 11 или 20 камней.
Для того чтобы делать ходы, у игроков есть только 80 камней, включая те, которые находятся в куче в начальный момент.
Игра завершается в тот момент, когда количество камней в куче становится не менее 61. Победителем считается игрок,
сделавший последний ход. В начальный момент в куче было S камней; 1 <= S <= 60.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Задание 19. Укажите количество значений S, при которых Петя может выиграть своим первым ходом.
Задание 20. Найдите два наименьших значения S, когда Петя имеет выигрышную стратегию, причём одновременно выполняются два условия:
– Петя не может выиграть за один ход;
– Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Задание 21. Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.  
'''
def f(s, m):
    if 61 <= s: return m % 2 == 0
    if m == 0: return 0
    #if 61 <= s <= 80: return m % 2 == 0  # перестраховка
    #if m == 0 or s > 80: return 0
    h = [f(s + 1, m - 1), f(s * 2, m - 1)] if s <= 40 else [f(s + 1, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
print('19)', len([s for s in range(1, 61) if f(s, 1)]))              # 19) 11
print('20)', *[s for s in range(1, 61) if not f(s, 1) and f(s, 3)])  # 20) 15 29
print('21)', *[s for s in range(1, 61) if not f(s, 2) and f(s, 4)])  # 21) 57