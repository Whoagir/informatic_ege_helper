// Автор: Зубов Н.С.
program ss;
var n, k, s, x, d : integer;
function F(n :integer): integer;                  
begin
     if (n <= 15) then Result := n*n + 11;
     if (n mod 2 = 0) and (n > 15) then Result := F(n div 2) + n * n * n - 5*n;
     if (n mod 2 <> 0) and (n > 15) then Result := F(n - 1) + 2 * n + 3;
end;
begin
     k := 0;
     For n := 1  to 1000 do
     begin
         x := F(n);
         d := 0;
         while x > 0 do begin
         
               if  x mod 10 =6 then 
               d := d + 1;
               x := x div 10
         end;
if d >=3
 then k := k + 1;
     end;
writeln(k);
end.