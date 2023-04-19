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
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {5, 6};
Line(6) = {6, 1};
Line(7) = {2, 5};
Line Loop(8) = {7, -4, -3, -2};
Plane Surface(9) = {8};
Line Loop(10) = {6, 1, 7, 5};
Plane Surface(11) = {10};

// Отметим подобласти и границы
Physical Surface("upper", 1) = {9};
Physical Surface("lower", 2) = {11};
Physical Line("upper_boundary", 1) = {3};
Physical Line("lower_boundary", 3) = {6};
Physical Point("fix_points") = {3, 4};
Physical Curve("interface") = {7};
