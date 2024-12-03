// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n = 1 then begin
    Result := 1;
    Exit;
  end;
  if n >0 then
    Result := 2* F(n-1)+n+3;
end;
begin
  writeln( F(19) )
end.

