# DeepLearningSpeechProcessing
Assignments of the Course Deep Learning Speech Processing 

## Assignment 0
Setting up librosa, soundfile and sounddevice modules

## Assignment 1
1. Recording sound using soundfile
2. Changing bit rate of sound files (quantization)
3. Resampling an audio signal

## Assignment 2
1. Create a function that computes an STFT of a time-domain signal
2. Use Overlap Add Synthesis to convert a time-frequency signal back to its time-domain representation
3. Compute Instantaneous Power and Total Energy of a signal
4. Find SNR - Signal to Noise Ratio
5. Prove Parseval's Theorem

## Assignment 3
### Part 1
1. SNR Calculation
2. Noisy Speech Generation having a desired SNR

### Part 2
1. Dataset Generation - 
a. Generated a Noisy and Clean speech dataset using the IEEE male and IEEE female speech signals and divides them into training, development and test sets.
b. Used three noise files provided and divide each noise signal in half, were the first half of each signal 
was be used to generate noisy speech for the training and development datasets, while the last half of each noise 
signal was used for the testing dataset.

2. Create Pytorch DataLoader for Train, Dev and Test Sets

### Part 3
1. Normalized and Standardized the Training and Development Set 
2. Used FFT Mask, IRM Mask, IBM Mask and Spectrograms for determining which target is best for Speech Enhancement
3. Replicated the results of the paper - Wang, Yuxuan, Arun Narayanan, and DeLiang Wang. "On training targets for supervised speech separation." IEEE/ACM transactions on audio, speech, and language processing 22.12 (2014): 1849-1858.
4. Technologies Used - Pytorch, Python, Librosa 

## Assignment 4
Using Kaldi on TIMIT dataset for Automatic Speech Recognition.

## Assignment 5
Using Google Speech-to-Text API for Automatic Speech Recognition on TIMIT Dataset
