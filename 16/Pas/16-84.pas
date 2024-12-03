// Автор: Зубов Н.С.
program ss;
var n,k: integer;
function F(n :integer): integer;                   
begin
     if (n <2) then Result := n;
     if (n mod 2 = 0) and (n >=2 ) then Result := F(n div 2) + 1; 
     if (n mod 2 <> 0) and (n >=2) then Result := F(3*n+1) + 1;
end;
   begin
     for n := 1  to 100 do begin
      F(n); 
      if F(n)>100 then k:=k+1;end;
        writeln(k);
  
end.