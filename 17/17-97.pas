// Автор: Зубов Н.С.
var k,max,i,m,d,a:integer;
begin
    k:=0;
    max:=0;
    for i:=777 to 3777 do begin 
         if (i mod 16 = 15) and  (i div 16 div 16  = 10) and  (i mod 11 <> 0) then begin
             k:=k+1;
             if max<i then
             max:=i;
         end;
    end;
    writeln(k,' ',max);
end.