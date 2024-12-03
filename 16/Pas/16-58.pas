// Автор: Зубов Н.С.
program ss;
var n, k, s, x, d : integer;
function F(n :integer): integer;                   
begin
     if (n >30) then Result := n*n + 3*n+5;
     if (n mod 2 = 0) and (n <=30 ) then Result := 2*F(n +1) +F(n +4); 
     if (n mod 2 <> 0) and (n <=30) then Result := F(n +2) + 3 *F(n +5);
end;
begin
     k := 0;
     For n := 1  to 1000 do
     begin
         x := F(n);
         d := 0;
         while x > 0 do begin
         
               if  x mod 10 =0 then 
               d := d + 1;
               x := x div 10
         end;
if d >=2 then k := k + 1;
     end;
writeln(k);
end.