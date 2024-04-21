zeros = [exp(1j*pi/3), exp(-1j*pi/3)];
poles = [0.9*exp(1j*pi/3), 0.9*exp(-1j*pi/3)];

num = poly(zeros);  
den = poly(poles);  

syms z w

Hz = poly2sym(num, z) / poly2sym(den, z);

Hw = subs(Hz, z, exp(1j*w));

Hw_mag = abs(Hw);
Hw_phase = angle(Hw);

disp('H(z):');
pretty(Hz_sym);

disp('H(w):');
pretty(Hw);

disp('Magnitude of H(w):');
pretty(Hw_mag);

disp('Phase of H(w) (in radians):');
pretty(Hw_phase);
