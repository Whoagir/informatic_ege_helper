// Автор: Зубов Н.С.
program abc;
var s,n,k:integer;
begin
 s:=0; 
 k:=0;
for n:=1361 to 7724 do begin
if (n mod 2=0) and (n mod 19<>0)
then
  k:=k+1;
s:=s+n;
end;
writeln(k,' ',s);
end.