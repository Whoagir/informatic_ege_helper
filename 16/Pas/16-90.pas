// Автор: Зубов Н.С.
program ss;
var n: integer;
function F(n :integer): integer;                   
begin
     if (n <2) then Result := 1;
     if (n mod 2 = 0) and (n >=2 ) then Result := F(n div 2) + 1; 
     if (n mod 2 <> 0) and (n >=2) then Result := F(n -1) + n;
end;
   begin
     for n := 1  to 100000 do begin
      F(n); 
      if F(n)=19 then 
        writeln(n);
  end;
end.