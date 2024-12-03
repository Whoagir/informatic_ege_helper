// Автор: Зубов Н.С.
var n,k,х:integer;
function F( n: integer ): integer;
begin
  if n <=3 then F := n
    else
  if (n mod 2=0) and (n>3) then
    F := F(n-1)+2*F(n div 2)
  else if (n mod 2<>0) and (n>3) then
    F := F(n-1)+F(n-3);
end;
begin
k:=0;
  for n:=1 to 1000 do begin 
    х:=F(n);
  if х <1000000000 then
    k:=k+1;
  end;
  writeln( k );
end.