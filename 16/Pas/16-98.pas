// Автор: Зубов Н.С.
program ss;
var n, k,s : integer;
function F(n :integer): integer;                   
begin
     if (n=0) then Result := 0;
     if (n mod 2 = 0) and (n > 0) then Result := F(n div 2)+3; 
     if (n mod 2 <> 0 ) and (n >0) then Result := 2* F(n -1) + 1;
end;
   begin
     k:=0;
     for n := 1  to 1000 do 
       begin
      F(n); 
      if F(n)<>0 then
        k:=k+1;
        end;
        writeln(k);
  
end.