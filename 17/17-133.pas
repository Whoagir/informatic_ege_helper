// Автор: В.М. Шелудько
var k, min, i : integer;
Begin
  k := 0;
  min := 11754;
  for i:=5913 to 11753 do 
    if (i mod 5 = 0) and (i mod 11 = 0) then
      if (i mod 13 <> 0) and (i mod 7 <> 0) then
        if (i mod 10 <> 0) and (i mod 22 <> 0) then begin
          k := k + 1;
          if i < min then
            min := i;
        end;
  writeln(k, ' ', min)
end.



