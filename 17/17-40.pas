// Автор: Зубов Н.С.
program n_1;
uses crt;
var i,m,d,n,p,k,min:integer;
begin
    k:=0;
    min:=9198;
    for i:=1871 to 9197 do begin
     m:=i;
     d:=0;
     while m>0 do begin
         m:=m div 16;
         d:=d+1;
     end;
     n:=i;
     p:=0;
     while n>0 do begin
         n:=n div 10;
         p:=p+1;
     end;
         if ((i mod 9 = 2) or (i mod 9 = 4)) and (d<>p) then begin
             k:=k+1;
             if min>i then
             min:=i;
         end;
    end;
    writeln(k,' ',min);
end.