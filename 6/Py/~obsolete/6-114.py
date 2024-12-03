cnt = 0
for dd in range(8, 100000, 10):
  d = dd #int(input())
  S = 5
  N = 7
  while S <= 3011:
    S = S + d
    N = N + 124
  #print(N)
  if N == 1247:
    cnt += 1
    print(cnt)
