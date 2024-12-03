// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n >16 then begin
    Result := n-3;
    Exit;
  end;
  if n <=16 then
    Result :=2*F(n+1)+2*n+3;
end;
begin
  writeln( F(2) )
end.