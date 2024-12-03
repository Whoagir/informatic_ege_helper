// Автор: Зубов Н.С.
program n_26;
uses crt;
var max,s,n:integer;
begin
max:=0;
s:=0;
for n:=3394 to 8599 do
if (n mod 3=1) and (n mod 7=5) then
begin
s:=s+n;
if (n>max) then
max:=n;
end;
writeln(max,' ',s);
end.
