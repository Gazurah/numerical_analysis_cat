import numpy as np
import matplotlib.pyplot as plt

def compute_fft(f1, f2, sample_rate, duration):
    t = np.linespace(0, duration, int(sample_rate * duration), endpoint = False) # time
    s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t) #signal
    
    fft_result = np.fft.fft(s)
    fft_freq = np.fft.fftfreq(len(t) , 1/sample_rate)
    
    pos_mask = fft_freq > 0
    fft_freq = fft_freq[pos_mask]
    fft_result = np.abs(fft_result[pos_mask])
    
    #plotting (signal)
    
plt.figure(figsize=(12,6))
plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(fft_freq, fft_result)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid()
plt.tight_layout()
plt.show()

f1 = 50
f2 = 120
sample_rate = 1000
duration = 1

compute_fft(f1,f2,sample_rate,duration)