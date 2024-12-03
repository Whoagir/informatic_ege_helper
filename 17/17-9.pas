// Автор: Зубов Н.С.
program n_1;
var i,k,min:integer;
begin
   k:=0;
   min:=10000;
   for i:= 1325 to 15367 do begin
       if (i mod 13 = 0) and (i mod 7 <> 0) and (i mod 23<> 0) and (i mod 17 <> 0) and (i mod 19 <> 0) then begin
       inc(k);
       if min>i then min:=i;
       end;
   end;
   writeln(k,' ',min);
end.