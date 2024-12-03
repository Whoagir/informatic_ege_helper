// Автор: Зубов Н.С.
function G (n:integer):integer;forward;
function F (n:integer):integer;
begin
if n<50 then 
  F:=n;
if n>49 then  
  F:=2*G(50-n div 2);
end;
function G(n:integer):integer;
begin
if n>40 then 
  G:=10;
if n<41 then
  G:=30+F(n+600 div n);
end;
begin
write(F(80));
end.