// Автор: Зубов Н.С.
program ss;
var n,k: integer;
function F(n :integer): integer;                   
begin
     if (n <=5) then Result := n;
     if (n mod 4 = 0) and (n >5 ) then Result :=n+F(n div 2-1); 
     if (n mod 4 <> 0) and (n >5) then Result := n+F(n+2);
end;
   begin
     for n := 1  to 20 do
      F(n);
      writeln(n);
  
end.