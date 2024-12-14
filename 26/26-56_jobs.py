f = open('26-56.txt')
v, k, n = map(int, f.readline().split())
f = sorted(map(int, f.readlines()[:n]))[::-1]

ar = [0]*k
dir_f = []
head = 0
for i in range(n):
    for j in range(head, head + k):
        if ar[j % k] + f[i] <= v:
            ar[j % k] += f[i]
            head = j
            break
    else:
        dir_f += [f[i]]
    head = head + 1
print(sum(dir_f), len(dir_f))

