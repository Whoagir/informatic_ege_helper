// Автор: Зубов Н.С.
var n,k:integer;
function F( n: integer ): integer;
begin
  if n <=3 then F := n
    else
  if (n mod 2=0) and (n>3) then
    F := 2*n*n+ F(n-1)
  else if (n mod 2<>0) and (n>3) then
    F := n*n*n*+n + F(n-1);
end;
Begin
k:=0;
begin
  for n:=1 to 1000 do
  if F(n)<10000000 then
    k:=k+1;
  writeln( k );
end;
end.

