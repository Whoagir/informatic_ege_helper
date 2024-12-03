// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n >15 then begin
    Result := n;
    Exit;
  end;
  if n <=15 then
    Result :=2*F(n+1)+5*n+2;
end;
begin
  writeln( F(2) )
end.