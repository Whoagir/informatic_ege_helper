// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n <=3 then begin
    Result := n;
    Exit;
  end;
  if n mod 3 =0 then
    Result := n*n*n + F(n-1);
  if n mod 3 =1 then
    Result := 4 + F(n div 3);
    if n mod 3 =2 then
    Result := n*n + F(n - 2);
end;
begin
  writeln( F(100) )
end.