// Автор: Зубов Н.С.
program ss;
var n, k, s, x, d : integer;
function F(n :integer): integer;                    
begin
     if (n <= 5) then Result := n + 15;
     if (n mod 2 = 0) and (n > 5) then Result := F(n div 2) + n * n * n - 1;
     if (n mod 2 <> 0) and (n > 5) then Result := F(n - 1) + 2 * n * n + 1;
end;
begin
     k := 0;
     For n := 1  to 1000 do
     begin
         x := F(n);
         d := 0;
         while x > 0 do begin
         
               if  x mod 10 =8 then 
               d := d + 1;
               x := x div 10
         end;
if d >=2 then k := k + 1;
     end;
writeln(k);
end.