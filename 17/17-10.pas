// Автор: Зубов Н.С.
var n,k,min:integer;
begin
k:=0;
min:=13766;
for n:= 1098 to 13765 do
if (n mod 2 = 0) and (n mod 7<>0)  and (n mod 11<>0) and (n mod 13<>0)  and (n mod 23<>0)
then begin
k:=k+1;
if n<min then
min:=n;
end;
write(k,' ',min);
end.