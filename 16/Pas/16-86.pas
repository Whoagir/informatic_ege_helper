// Автор: Зубов Н.С.
program ss;
var n,k: integer;
function F(n :integer): integer;                   
begin
     if (n <2) then Result := 1;
     if (n mod 2 = 0) and (n >=2 ) then Result := F(n div 2) + 1; 
     if (n mod 2 <> 0) and (n >=2) then Result := F(n -3) + 3;
end;
   begin
     for n := 1  to 100000 do begin
      F(n); 
      if F(n)=12 then k:=k+1;end;
        writeln(k);
  
end.