// Автор: Зубов Н.С.
program n_1;
var i,n,d,m,p,k,s:integer;
begin
    k:=0;
    s:=0;
 for i:=10 to 6000 do
   begin
        n:=i;
        d:=0;
        p:=0;
          while n>0 do
          begin
          p:=n mod 5;
          if p<>2 then 
          d:=d+1;
          n:=n div 5;
          end;
 if (i mod 6 = 0) and (d=0)  then begin 
           inc(k);
           s:=s+i;
           end;
    end;
    writeln(k,' ',s);
end.