def control_sum(num):
    a = list(map(int, list(str(num))))
    sum_even_ind = sum(a[-1::-2])
    sum_odd_ind = sum(map(lambda x: 2 * x % 10 + 2 * x // 10, a[-2::-2]))
    return sum_even_ind + sum_odd_ind


num = 1000_0000_0000_0000
num += 1
while control_sum(num) != 25:
    num += 1
print(num % 10**15)
