def F(n):
    if n<=70:
        return (F(n+2))+(2*F(3*n))
    if n>70:
        return n-50
print(F(40))