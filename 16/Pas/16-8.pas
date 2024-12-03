// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n >18 then begin
    Result := n;
    Exit;
  end;
  if n <=18 then
    Result :=3*F(n+1)+n+8;
end;
begin
  writeln( F(9) )
end.