// Автор: Зубов Н.С.
program n_1;
var k,max,i,m,d,a:integer;
begin
    k:=0;
    max:=0;
    for i:=10 to 9999 do begin
     m:=i;
     d:=0;
     while m>0 do begin
     a:= m mod 2;
     if a=0  then  d:=d+1;
     m:=m div 2;
     end;
         if (i mod 2 = 1) and (d=5) and (i mod 3 = 0) and (i mod 11 = 0) then begin
             k:=k+1;
             if max<i then
             max:=i;
         end;
    end;
    writeln(k,' ',max);
end.