// Автор: Зубов Н.С.
program abc;
var n,k,max:integer;
begin
k:=0;
max:=0;
for n:=1305 to 14063 do
if ((n mod 2=0) or (n mod 3=0)) and ((n mod 7<>0) and (n mod 11<>0) and (n mod 17<>0) and (n mod 23<>0))
then begin
k:=k+1;
if max<n then
max:=n;
end;
writeln(k,' ',max);
end.
