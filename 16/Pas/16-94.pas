// Автор: Зубов Н.С.
program ss;
var n, min: integer;
function F(n :integer): integer;                   
begin
     if (n <2) then Result := 1;
     if (n mod 3 = 0) and (n >=2 ) then Result := F(n div 3) - 1; //F(n/3)
     if (n mod 3 <> 0) and (n >=2) then Result := F(n -1) + 17;
end;
   begin
     min:=1000000;
     for n := 1  to 100000 do 
    begin
      F(n); 
      if (F(n)=110) and (n<min)  then 
        min:=n; 
  end;
  writeln(min);
end.