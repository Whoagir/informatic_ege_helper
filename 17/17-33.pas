// Автор: Зубов Н.С.
uses crt;
var n,m,max,min,d:integer;
begin
max:=0;
min:=10000;

for n:=1000 to 9999 do begin
m:=n;
d:=0;
while m > 0 do begin
if m mod 3 >= 0 then
d:=d+1;
m:=m div 3;
end;
if (d=8) and (n mod 5<>0) and (n mod 7<>0) and (n mod 11<>0) then begin
if max<n then
max:=n;
if min>n then
min:=n;
end;
end;
writeln(min,' ',max);
end.