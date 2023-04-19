// Параметры
LX = 0.02;
dy = 0.002;
LY = 0.01+dy;
p1 = LY/50;
p2 = LY/100;
// Создадим расчетную область
Point(1) = { 0, 0, 0, p1};
Point(2) = { 0, dy, 0, p2};
Point(3) = { 0, LY, 0, p1};
Point(4) = { LX, LY, 0, p1};
Point(5) = { LX, dy, 0, p2};
Point(6) = { LX, 0, 0, p1};
Line(1) = {1, 3};
//Line(2) = {2, 3};
Line(2) = {3, 4};
//Line(4) = {4, 5};
Line(3) = {4, 6};
Line(4) = {6, 1};
//Line(7) = {2, 5};
Line Loop(5) = {1, 2, 3, 4};
Plane Surface(6) = {5};
// Отметим подобласти и границы

//+
Recursive Delete {
  Point{5}; Point{2}; 
}
//+
Physical Point("fix_point", 7) = {3, 4};
//+
Physical Curve("fixed_walls", 8) = {1, 3};
//+
Physical Curve("moving_walls", 9) = {2, 4};
//+
Physical Surface("material", 10) = {6};
