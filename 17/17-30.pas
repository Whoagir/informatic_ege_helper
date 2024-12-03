// Автор: Зубов Н.С.
program n_30;
uses crt;
var min,s,n:integer;
begin
min:=9483;
s:=0;
for n:=1529 to 9482 do
if (n mod 2=1) and (n div 2 mod 2=0)  and (n mod 5=3)
then begin
s:=s+n;
if n<min
then
min:=n;
end;
writeln(min,' ',s);
end.