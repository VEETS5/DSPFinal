import numpy as np
import matplotlib.pyplot as plt

poles = [0, 0]  
zeros = [np.exp(1j * np.pi/3), np.exp(-1j * np.pi/3)]

fig, ax = plt.subplots(figsize=(6, 6))

unit_circle = plt.Circle((0, 0), 1, fill=False, linestyle='--', color='gray')
ax.add_artist(unit_circle)

ax.scatter(np.real(poles), np.imag(poles), marker='o', facecolors='none', edgecolors='r', s=50, label='Poles')
ax.scatter(np.real(zeros), np.imag(zeros), marker='x', color='b', s=50, label='Zeros')

ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_title('Pole-Zero Plot')
ax.legend()
ax.axis('equal') 
ax.grid()
plt.show()