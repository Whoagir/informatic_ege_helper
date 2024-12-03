// Автор: Зубов Н.С.
program kk;
uses crt;
var k,sum,n:integer;
begin
k:=0;
sum:=0;
for n:=3672 to 9117 do
if (n mod 3=2) and (n mod 5=4) then begin
k:=k+1;
sum:=sum+n;
end;
writeln (k,' ',sum);
end.
