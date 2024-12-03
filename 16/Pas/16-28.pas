// Автор: Зубов Н.С.
var s, n: integer;
procedure F( n: integer );
begin
  // writeln(2*n+1);
  s := s + 2*n+1;
  if n > 1 then begin
    // writeln(3*n-8);
    s := s + 3*n-8;
    F(n-1);
    F(n-4);
  end;
end; 
begin
  n := 0;
  repeat
    n := n + 1;
    s := 0;
    F(n);
  until s > 5000000;
  writeln( n, ' ', s); 
end.