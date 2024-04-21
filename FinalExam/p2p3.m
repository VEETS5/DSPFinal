Fs = 50;  
M = 50;  

syms n;

h_ideal = (sin(2*pi*15*n/Fs) - sin(2*pi*10*n/Fs)) / (pi*n);
w = 0.54 - 0.46*cos(2*pi*n/M);

h = h_ideal * w;

h_eq = simplify(h);

h_coeffs = zeros(1, 4);

%Handle the case when n=0
h_coeffs(1) = double(limit(h_eq, n, 0));
%Handle the rest
for i = 2:4
    h_coeffs(i) = double(subs(h_eq, n, i-1));
end

disp('First 4 coefficients of h(n):');
disp(h_coeffs);