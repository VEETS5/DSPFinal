Fs = 50;  
M = 50;  

syms n;

h_ideal = (sin(2*pi*15*n/Fs) - sin(2*pi*10*n/Fs)) / (pi*n);
h_ideal(n==0) = (15 - 10) / Fs;

w = 0.54 - 0.46*cos(2*pi*n/M);

h = h_ideal * w;

h_eq = simplify(h);

disp('Equation for h(n):');
pretty(h_eq);