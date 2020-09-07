w = 10; %lbs
a = 1.516;
b = 1;
c = 1.5;
d = 0.363;
e = 1;
theta4 = deg2rad(17.8);
theta2 = deg2rad(22.5);

syms Mm Ax Ay Bx By Cx Cy Dx Dy
eq1  = Mm == w* (e+c*cos(theta4));
eq2  = Cx + Dx == 0;
eq3  = Cy + Dy == w;
eq4  = b * Bx == w * e;
eq5  = Bx + Ax == 0;
eq6  = By + Ay == w;
eq7  = Mm + c * cos(theta4) * Bx == 0;
eq8  = Cx + Bx == 0;
eq9  = Cy + By == 0;
%eq10 =
%eq11 = 

[A,B] = equationsToMatrix([eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9], [Mm, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy])

double(B(1)) % motor torque