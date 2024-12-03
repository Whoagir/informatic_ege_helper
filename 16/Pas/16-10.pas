// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n >12 then begin
    Result := 2*n-5;
    Exit;
  end;
  if n <=16 then
    Result :=2*F(n+2)+n-4;
end;
begin
  writeln( F(1) )
end.