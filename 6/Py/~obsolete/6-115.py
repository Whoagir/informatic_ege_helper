for ss in range(1, 100000):
  S = ss #int(input())
  S = S // 8
  N = 2
  while S <= 102:
    S = S + 4
    N = N * 2 - 1
  #print(N)
  if N == 257:
    print(ss)

