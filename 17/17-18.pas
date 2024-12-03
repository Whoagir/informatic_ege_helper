// Автор: Зубов Н.С.
program n_1;
var i,k,min:integer;
begin
   k:=0;
   min:=5321;
   for i:= 980 to 5320 do begin
       if ((i mod 4 = 0)or(i mod 5=0)) and ((i mod 11 <> 0) and (i mod 17<> 0) and (i mod 19 <> 0) and (i mod 23 <> 0)) then begin
       inc(k);
       if min>i then min:=i;
       end;
   end;
   writeln(k,' ',min);
end.