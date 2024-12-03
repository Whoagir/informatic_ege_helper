// Автор: Зубов Н.С.
var x,s,n,k:integer;
function F( n: integer ): integer;
begin
if n >25 then F:=n*n+2*n+1
else 
if (n mod 2 =0) and (n<26) then F:= 2*F(n+1)+F(n+3)
else 
F:=F(n+2)+3*F(n+5);
end;
begin
k:=0;
for n:=1 to 1000 do begin
x:=F(n);
s:=1;
while x>0 do
   begin
if x mod 10= 0 then
s:=0;
x:=x div 10;
  end;
k:=k+s;
end;
writeln(k);   
end.