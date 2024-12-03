// Автор: Зубов Н.С.
program aca;
var n,k,min:integer;
begin
k:=0;
min:=8368;
for n:=1170 to 8367 do
if ((n mod 3=0) or (n mod 7=0)) and (n mod 11 <> 0) and (n mod 13 <> 0) and (n mod 17 <> 0) and (n mod 19 <> 0)
then begin
k:=k+1;
if n<min then
min:=n;
end;
writeln(k,' ',min);
end.