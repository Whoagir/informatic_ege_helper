// Автор: Зубов Н.С.
program n_1;
var i,n,d,m,p,k,max:integer;
begin
    k:=0;
    max:=0;
    for i:=127 to 9852 do begin
        n:=i;
        d:=0;
          while n>0 do begin
          n:=n div 10;
          d:=d+1;
          end;
        m:=i;
        p:=0;
          while m>0 do begin
          m:=m div 8;
          p:=p+1;
          end;
        if ((i mod 3 = 0) and (i mod 9<>0)) and (d=p) then begin
            inc(k);
            max:=i;
        end;
    end;
    writeln(k,' ',max);
end.