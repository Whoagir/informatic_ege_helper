// Автор: В.М. Шелудько
var k, s, min, i : integer;
Begin
  k := 0;
  min := 8186;
  for i:=6391 to 8185 do 
    if (i mod 11 = 0) or (i mod 17 = 0) then
      if (i mod 13 <> 0) and (i mod 2 <> 0) then
        if (i mod 14 <> 0) and (i mod 34 <> 0) then begin
          k := k + 1;
          s := s + i;
          if i < min then
            min := i;
        end;
  writeln( trunc(s/k), ' ', min)
end.




