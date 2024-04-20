import numpy as np
import matplotlib.pyplot as plt

F = np.linspace(0, 25, 1000) 

H_IDEAL = np.zeros_like(F)
H_IDEAL[(np.abs(F) >= 10) & (np.abs(F) <= 15)] = 1

plt.figure(figsize=(8, 4))
plt.plot(F, H_IDEAL, linewidth=2)
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Ideal Bandpass Filter Frequency Response')
plt.grid(True)
plt.xlim(0,25)
plt.ylim(-0.1, 1.1)
plt.xticks(np.arange(0, 26, 5))
plt.show()