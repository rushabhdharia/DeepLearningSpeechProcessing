import sounddevice as sndev
import soundfile as sndfl
import librosa


duration = 7
fs = 44100

# Q1 part1
myrecording = sndev.rec(int(duration * fs), samplerate=fs, channels=1)
sndev.wait()

sndev.play(myrecording, fs)

# Q1 part 2
sndfl.write("pcm32.wav", myrecording, fs, 'PCM_32')
sndfl.write("pcm16.wav", myrecording, fs, 'PCM_16')
sndfl.write("pcmU8.wav", myrecording, fs, 'PCM_U8')

# Q1 part 3
## 32 bit rate sound is more crisper with less noise in the background
## whereas 8 bit rate sound is less clear with more noise in the background
## PCM_32 sounds the best and PCM_U8 sounds the worst as the bit rate is decreased

# Q2 part 1
data, fs = librosa.load("pcm32.wav", sr=fs)

y_22050 = librosa.resample(data, fs, 22050)
sndfl.write("y_22050.wav", y_22050, 22050, 'PCM_32')

y_11025 =  librosa.resample(data, fs, 11025)
sndfl.write("y_11025.wav", y_11025, 11025, 'PCM_32')

y_5512  = librosa.resample(data, fs, 5512)
sndfl.write("y_5512.wav", y_5512, 5512, 'PCM_32')

y_2250 = librosa.resample(data, fs, 2250)
sndfl.write("y_2250.wav", y_2250, 2250, 'PCM_32')

# Q2 part 2
## As sampling rate decreases the quality of the signal decreases
## This happens because we sample/reduce the continuous signal to a discrete signal
## Because of this reduction the signal quality decreases
## y_22050 sounds the best and y_2250 sounds the worst (no sound because of aliasing)