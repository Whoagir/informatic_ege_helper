K = 100
P = set(range(44*K, 49*K+1))
Q = set(range(28*K, 53*K+1))
U = set(range(100*K))
A = U.copy()
for x in U:
  if (((x in A) <= (x in P)) or (x in Q)) == False:
    A.remove(x)
# print(A)
print( len([x for x in A])/K )