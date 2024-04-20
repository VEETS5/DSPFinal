import numpy as np

def H_mag(omega, K=1):
    numerator = np.abs((np.exp(1j * omega) - np.exp(1j * np.pi/3)) * (np.exp(1j * omega) - np.exp(-1j * np.pi/3)))
    denominator = np.abs((np.exp(1j * omega) - 0.9 * np.exp(1j * np.pi/3)) * (np.exp(1j * omega) - 0.9 * np.exp(-1j * np.pi/3)))
    return K * numerator / denominator

H_0 = H_mag(0)
H_pi_3 = H_mag(np.pi/3)
H_pi_6 = H_mag(np.pi/6)
H_pi_2 = H_mag(np.pi/2)

print(f"|H(0)| = {H_0:.4f}")
print(f"|H(pi/3)| = {H_pi_3:.4f}")
print(f"|H(pi/6)| = {H_pi_6:.4f}")
print(f"|H(pi/2)| = {H_pi_2:.4f}")