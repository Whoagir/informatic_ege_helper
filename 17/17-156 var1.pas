// Автор В.Н. Шубинкин

##
var a := ReadLines('17-2.txt').Select(t -> t.ToInteger).ToArray;
var maxEl := a.Max;
print(a.CountOf(maxEl), a.IndexMax + 1)

{ Рекомендую также ознакомиться с эффективным однопроходным алгоритмом,
  без использования массива var2}