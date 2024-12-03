// Автор: Зубов Н.С.
function F( n: longint): longint ;
begin
  if n =0 then begin
    Result :=1;
    Exit;
  end;
  if n>0  then
    Result := 2*F(1-n)+3*F(n-1)+2;
  if n<0then
    Result := - F(-n);
end;
begin
  writeln( F(50) )
end.
