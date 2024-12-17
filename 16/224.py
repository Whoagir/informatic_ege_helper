F={1:1}
for n in range(2,24):
    if n%2==0:
        F[n]=n*n+F[n-1]
    else:
        F[n]=F[n-1]+2*F[n-2]
print(F)