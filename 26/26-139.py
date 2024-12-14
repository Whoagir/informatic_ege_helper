# Автор: Л. Шастин

f = open('26-139.txt')
n, k = map(int, f.readline().split())
a = sorted(list(map(int, x.split())) for x in f)
max_right = current = count = 0
while max_right < k:
    curr_max_right = a[current][1]
    while current < n and a[current][0] <= max_right + 1:
        curr_max_right = max(curr_max_right, a[current][1])
        current += 1
    count += 1
    max_right = curr_max_right
print(n - count, sum(x[0] <= k and x[1] >= k for x in a))

