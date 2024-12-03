// Автор: В.М. Шелудько
var min, max, i : integer;
Begin
  min := 13020;
  max := 3520;
  for i:=3521 to 13019 do 
    if (i mod 6 = 0) and (i mod 15 = 0) then
      if (i mod 9 <> 0) and (i mod 12 <> 0) then
        if (i mod 17 <> 0) and (i mod 21 <> 0) then begin
          if i < min then
            min := i;
          if i > max then
            max := i;
        end;
  writeln(max, ' ', min)
end.

