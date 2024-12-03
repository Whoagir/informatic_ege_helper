// Автор: Зубов Н.С.
var count: integer;
procedure F( n: integer );
begin
  // write('*');
  count := count + 1;
  if n >= 1 then begin
    // write('*');
    count := count + 1;
    F(n-1);
    F(n-2);
  end;
end;
begin
  count := 0;
  F(28);
  writeln(count);
end.

