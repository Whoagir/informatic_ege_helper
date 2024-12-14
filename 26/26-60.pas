// Автор: А. Богданов
##
assign(input, '26-60.txt');
var (K,N) := ReadInteger2;

var place := ReadArrInteger(K); // мест на направлении

var group := place
  .Select(p -> new List<integer>(p))  // пустой список группы
  .ToArray;  // рейтинг школьников по направлению

loop N do begin
  var (ball,idGroup) := ReadInteger2;
  group[idGroup].Add(ball); // в список группы
end;

var students := 0; var maxConcurs := 0.0; var ball := 0;
for var i := 0 to K-1 do begin
  var (g,p) := (group[i],place[i]);
  
  g.Sort();
  g.Reverse();
  
  var concurs := g.Count/p;
  if concurs>maxConcurs then begin
    maxConcurs := concurs;
    ball := g[p-1];
  end;

  students += min(place[i],g.Count);
end;

print(students, ball)