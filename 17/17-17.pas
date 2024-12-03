// Автор: Зубов Н.С.
program n_1;
var i,k,min:integer;
begin
   k:=0;
   min:=9999999;
   for i:= 1056 to 7563 do begin
       if ((i mod 3 = 0)or(i mod 11=0)) and ((i mod 13 <> 0) and (i mod 17<> 0) and (i mod 19 <> 0) and (i mod 23 <> 0)) then begin
       inc(k);
       if min>i then min:=i;
       end;
   end;
   writeln(k,' ',min);
end.