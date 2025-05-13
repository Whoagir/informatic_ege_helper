def f(n):
    if n<1:
        return n
    if n>=1 and n%2==0:
        return n+3*f(n-3)
    if n>=1 and n%2!=0:
        return 5*n+2*f(n-5)

print(f(30))