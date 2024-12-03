// Автор: Зубов Н.С.
program ooo;
var s,k,n:integer;
begin
k:=0;
s:=0;
for n:=1905 to 9868 do
if (n mod 3=0) and (n mod 23<>0) then begin
k:=k+1;
s:=s+n;
end;
writeln (k,' ',s);
end.