// Автор: Зубов Н.С.
program ooo;
var s,k,n:integer;
begin
k:=0;
s:=0;
for n:=1840 to 9052 do
if (n mod 7=0) and (n mod 23<>0) then begin
k:=k+1;
s:=s+n;
end;
writeln (k,' ',s);
end.