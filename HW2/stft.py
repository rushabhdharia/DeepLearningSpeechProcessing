import numpy as np
import librosa
import sys
import matplotlib.pyplot as plt

def stft(signal, n, window_type, window_length, L, fs):
	if window_type == "hamming":
		w_m = np.hamming(window_length)
	else:
		return

	w_m =  np.flip(w_m)
	X = []
	i = 0
	k = 1
	N = len(signal)

	while i<N:
		if (window_length+i<N):
			segment = signal[i: window_length+i]
		else:
			temp = signal[i:]
			segment = np.zeros(w_m.shape)
			segment[:temp.shape[0]] = temp
		prod = np.multiply(segment, w_m)
		x = np.sum(prod*np.exp(-2j*np.pi*k*n/N))
		x = 20*np.log10(x)
		X.append(x)
		k += 1
		i += L

	print(len(X))
	powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(X, Fs = fs)
	plt.xlabel('Time')
	plt.ylabel('Frequency')
	plt.plot(X)
	plt.show()

	# plot.subplot(211)
	# plot.title('Spectrogram of a wav file with piano music')

	# plot.plot(signalData)
	# plot.xlabel('Sample')
	# plot.ylabel('Amplitude')

	 
	# plot.subplot(212)
	# plot.specgram(signalData,Fs=fs)
	# plot.xlabel('Time')
	# plot.ylabel('Frequency')
	#plot.show()
	
	return

def main():
	signal, fs = librosa.load("speech2.wav")
	
	N = [256, 256, 512, 1024, 2048]
	window_type = "hamming"
	window_length = [10, 20, 40, 80, 160]
	L = [5, 10, 20, 40, 80]
	for i in range(len(N)):
		stft(signal, N[i], window_type, window_length[i], L[i], fs)
		sys.exit()
		input("Press Enter to continue...")
		

if __name__ == '__main__':
	main()
	