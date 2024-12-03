// Автор: Зубов Н.С.
program n_1;
uses crt;
var s,max,n:integer;
begin
max:=0;
s:=0;
for n:=2807 to 8558 do
if (n div 2 mod 2=1) and (n mod 9=5) and (n mod 2=1)
then
begin
s:=s+n;
if max<n then
max:=n;
end;
writeln (max,' ',s);
end.