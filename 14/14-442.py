# Автор: П. Финкель

s=0
for  x  in range(72):
  for  y in range(82):
    l=[]
    a=2*71**3+x*71**2+x*71**2+3
    b=4*73**3+8*73**2+x*73+4
    c=7*78**3+x*78**2+6*78+5
    d=3*81**3+x*81**2+y*81+9
    t=a+b+c-d

    if t%1234==0 and t>0:
      print(x,y,t,' = ',l)
      s+=x+y
print(s)