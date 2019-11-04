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
