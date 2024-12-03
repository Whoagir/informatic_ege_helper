// Автор: Зубов Н.С.
program n_54;
var k,n,s:integer;
begin
k:=0;
s:=0;
for n:=2595 to 8401 do begin
if (n mod 2=0) and (n mod 13<>0) then
k:=k+1;
s:=s+n;
end;
writeln(k,' ',s);
end.