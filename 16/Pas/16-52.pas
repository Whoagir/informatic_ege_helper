// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n <= 1 then begin
    Result := 1;
    Exit;
  end;
  if (n >1) and (n mod 2=0) then
    Result :=n + F(n-1)
  else
    Result :=n*n + F(n-2)
end;
begin
  writeln( F(80) )
end.
