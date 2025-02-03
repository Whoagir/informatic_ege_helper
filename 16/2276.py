def F(n):
    if n>15:
        return n*n-5
    if n<=15:
        return n*F(n+2)+n+F(n+3)
v=str(F(1))
v1=int()
