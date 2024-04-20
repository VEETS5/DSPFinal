import numpy as np
import matplotlib.pyplot as plt

def H_omega(w, K=1):
    z = np.exp(1j * w)
    numerator = (z - np.exp(1j * np.pi/3)) * (z - np.exp(-1j * np.pi/3))
    denominator = (z - 0.80 * np.exp(1j * np.pi/3)) * (z - 0.80 * np.exp(-1j * np.pi/3))
    H = K * numerator / denominator
    magnitude = np.abs(H)
    phase = np.angle(H)
    return H, magnitude, phase

K = 1 
w = np.linspace(-np.pi, np.pi, 100)

H, mag, phase = H_omega(w, K)
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(w, mag)
ax[0].set_title('Magnitude Response')
ax[0].set_xlabel('Frequency omega')
ax[0].set_ylabel('Magnitude')

ax[1].plot(w, phase)
ax[1].set_title('Phase Response')
ax[1].set_xlabel('Frequency omega')
ax[1].set_ylabel('Phase')

plt.tight_layout()
plt.show()