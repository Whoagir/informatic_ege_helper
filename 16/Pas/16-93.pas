﻿// Автор: Зубов Н.С.
program ss;
var n, s : integer;
function F(n :integer): integer;                   
begin
     if (n <2) then Result := 1;
     if (n mod 3 = 0) and (n >=2 ) then Result := F(n div 3) - 1; 
     if (n mod 3 <> 0) and (n >=2) then Result := F(n -1) + 7;
end;
   begin
     for n := 1  to 100000 do begin
      F(n); 
      if F(n)=111 then 
        writeln(n);
  end;
end.