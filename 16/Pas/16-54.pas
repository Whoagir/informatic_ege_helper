// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n >25  then 
    Result := 2*n*n*n+n*n
  else
    Result :=F(n+2)+2*F(n+3)
end;
begin
  writeln( F(2) )
end.
