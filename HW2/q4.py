import numpy as np
import librosa

signal, fs = librosa.load("speech2.wav")

total_energy_speech = np.sum(np.square(signal))
print(total_energy_speech)


# def dft(signal):
#     X = []
#     N = len(signal)
#     for k in range(N):
#         temp = 0
#         for n in range(N):
#             temp += signal[n]*np.exp(-2j*np.pi*k*n/N)
#         X.append(temp)
#     return X


def DFT(x):
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


X = np.empty(signal.shape, dtype = 'complex')
i = 0 
step = 1024 # 2^10
N = len(X)
n = np.arange(N)
k = n.reshape((N,1))
nk = n * k
print(nk.shape)

while i+step<len(signal):
    X[i:i+step] = DFT(signal[i:i+step], i, i+step)
    i += step

X[i:] = DFT(signal[i:], i, len(signal))

X = dft(signal)
power_dft = np.sum(np.square(X))/len(signal)





