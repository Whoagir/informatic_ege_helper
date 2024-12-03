// Автор: Зубов Н.С.
var k,max,i,m,d,a:integer;
begin
    k:=0;
    max:=0;
    for i:=100 to 1000000 do begin 
         if (i mod 16 = 10) and  (i div 16 div 16 div 16 div 16 = 11) and  (i mod 12 <> 0) then begin
             k:=k+1;
             if max<i then
             max:=i;
         end;
    end;
    writeln(k,' ',max);
end.