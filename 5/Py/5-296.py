# Автор В.Н. Шубинкин

def is_correct(num):
    a = list(map(int, list(str(num))))
    sum_even_ind = sum(a[-1::-2])
    sum_odd_ind = sum(map(lambda x: 2 * x % 10 + 2 * x // 10, a[-2::-2]))
    return (sum_even_ind + sum_odd_ind) % 10 == 0


num = 1234_5678_9101_1121
num += 1
while not is_correct(num):
    num += 1
print(num % 10**8)
