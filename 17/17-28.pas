
p// Автор: Зубов Н.С.rogram n_1;
uses crt;
var i,k,max:integer;
begin
    max:=0;
    k:=0;
    for i:=3439 to 7410 do  begin
        if ((i mod 2)<>(i mod 6)) and ((i mod 9=0) or (i mod 10=0) or (i mod 11=0)) then begin
            k:=k+1;
            if max<i then max:=i;
        end;
    end;
    writeln(k,' ',max);
end.