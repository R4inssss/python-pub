import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

st = 0
et = 1
rate = 90
time = np.arange(st, et, 1 / rate)
phaseshift = 0
fq = 100
amp = 1
sinewave = amp * np.sin(2 * np.pi * fq * time + phaseshift)
figure(figsize=(20, 6), dpi=80)
plt.plot(time, sinewave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Caterpillar Wave')
plt.grid(True)
plt.show()
