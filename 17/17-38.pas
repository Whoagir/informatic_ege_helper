// Автор: Зубов Н.С.
program abc;
var k,max,n:integer;
begin
max:=0;
k:=0;
for n:=2461 to 9719 do
if ((n div 100) mod 10<>1) and ((n div 100) mod 10<>9) and ((n mod 100) div 10>=3) and  ((n mod 100) div 10<=7)
then 
  begin
    k:=k+1;
    if n>max then
      max:=n;
  end;
  writeln(k,' ',max);
end.