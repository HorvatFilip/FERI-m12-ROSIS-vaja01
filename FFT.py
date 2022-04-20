import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fftfreq
from scipy.fftpack import fft
from scipy.io import wavfile


def Plot(X, fs):
    N = len(X)
    n = np.arange(N)
    T = N/fs
    freq = n/T 

    plt.figure(figsize = (8, 6))
    #plt.stem(freq, abs(X), 'b',markerfmt=" ", basefmt="-b")
    #plt.xlim([-10, 66000])
    plt.plot(abs(X),'r')
    plt.xlabel('Freq (Hz)')
    plt.ylabel('DFT Amplitude |X(freq)|')
    plt.show()


'''
sr = 100
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)


N = len(x)
selected_sin_freq = np.arange(0,N)
selected_sin_freq = selected_sin_freq[::30]
'''
filename = "/home/ph5151/Desktop/FERI/Semester02/RacunalniskaObdelavaSignalovInSlik/Vaje/Vaja01/FERI-m12-ROSIS-vaja01/audiofiles/CantinaBand3.wav"
filename = "/home/ph5151/Desktop/FERI/Semester02/RacunalniskaObdelavaSignalovInSlik/Vaje/Vaja01/FERI-m12-ROSIS-vaja01/audiofiles/2022-04-12-01:26:37.wav"
filename = "/home/ph5151/Desktop/FERI/Semester02/RacunalniskaObdelavaSignalovInSlik/Vaje/Vaja01/FERI-m12-ROSIS-vaja01/audiofiles/1.)_a.wav"

fs, x = wavfile.read(filename)

if len(x.shape) > 1:
    print(x.shape)
    x = x.T[0]
X = fft(x)
#Xfreq = fftfreq(x, 1/fs)
#plt.plot(Xfreq, np.abs(X))
#plt.show()
Plot(X[:len(X)//2],fs)
#Plot(X,fs)

'''
n = X
calculations = {}
for k, freq in enumerate(selected_sin_freq):
    for n, x_ in enumerate(x):
        e = np.exp(-1j * 2 * np.pi * k * n / N)
        X[k] = X[k] + np.dot(e, x_)

Plot(X[:len(X)//2],fs)
'''
