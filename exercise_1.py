m = 1500
v = 22.2
g = 9.81
u = 0.015
c = 0.31
A = 1.97
p = 1.204

Fr = m * g * u 
print("Die Reibkraft beträgt: ", Fr)
Fl = c*A*p*v*v*0.5
print("Der Luftwiderstand beträgt: ", Fl)
W = (Fr + Fl) * v
print("Die verbarauchte Energie beträgt: ", W)
