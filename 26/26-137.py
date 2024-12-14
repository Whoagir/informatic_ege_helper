# Автор: Л. Шастин

f = open('26-137.txt')
k = int(f.readline())
n = int(f.readline())
a = sorted(list(map(int, f.readline().split())) for _ in range(n))
numbers = [0] * k
free_time = {minute: 0 for minute in range(1, 1441)}
count = 0
for start, end, quantity in a:
    if len([time for time in numbers if time < start]) >= quantity:
        while quantity > 0:
            for number in range(k):
                if numbers[number] < start:
                    numbers[number] = end
                    quantity -= 1
                    for minute in range(start, end + 1):
                        free_time[minute] += 1
                    break
        count += 1
print(count, sum([free_time[minute] < k for minute in free_time]))
