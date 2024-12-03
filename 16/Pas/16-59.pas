// Автор: Зубов Н.С.
program ss;
var n, k, s, x : integer;
function F(n :integer): integer;
begin
     if n > 30 then Result := n * n + 5 * n + 4;
     if (n mod 2 = 0) and (n <= 30) then Result := F(n + 1) + 3 * F(n + 4);
     if (n mod 2 <> 0) and (n <=30) then Result := 2*F(n + 2) +  F(n + 5);
end;
begin
     k := 0;
     For n := 1  to 1000 do
     begin
         x := F(n);
         s := 0;
         while (x > 0) do begin
         s := s + (x mod 10);
         x := x div 10;
         end;
         if (s = 27) then
            k := k + 1;
     end;
writeln(k);
end.