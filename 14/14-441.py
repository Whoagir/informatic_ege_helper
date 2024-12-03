# Автор: П. Финкель

s=0
for  x  in range(1,58):
  for  y in range(72):
    a=3*58**3+4*58**2+x*58+5
    b=1*61**3+2*61**2+x*61+7
    c=x*67**3+4*67**2+5*67+6
    d=x*72**3+5*72**2+y*72+7
    t=a+b+c-d

    if t%363==0 and t>0:
      print(x,y,t)
      s+=x+y

print(s)