// Автор: Зубов Н.С.
var k,max,i,m,d,a:integer;
begin
    k:=0;
    max:=-5001;
    for i:=-5000 to 5000 do begin 
         if (i mod 16 = 11) and  (i mod 6 <> 0) and  (i mod 5 = 0) and  (i mod 7 = 0) then begin
             k:=k+1;
             if max<i then
             max:=i;
         end;
    end;
    writeln(k*2,' ',max);
end.

