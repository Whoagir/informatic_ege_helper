// Автор: Зубов Н.С.
var k,max,i,m,d,a:integer;
begin
    k:=0;
    max:=0;
    for i:=100 to 10000 do begin 
         if (i mod 10 = 3) and  (i mod 8 = 7) and  (i mod 13 <> 0) and  (i mod 16 <> 0) and  (i mod 19 <> 0) and  (i mod 21 = 0)then begin
             k:=k+1;
             if max<i then
             max:=i;
         end;
    end;
    writeln(k,' ',max);
end.