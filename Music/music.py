import wave
import numpy as np

# Sample rate and duration (in seconds)
sample_rate = 44100
duration = 0.85
duration2 = 1.5
duration3=0.5


# Create an empty array to store the samples
samples = np.array([])

# Define the frequency and amplitude of a sine wave
frequency = 510
amplitude = 5000

# Generate samples for the sine wave
for i in range(int(sample_rate * duration)):
    sample = amplitude * np.sin(2 * np.pi * frequency * i / sample_rate)
    samples = np.append(samples, sample)



# Create a new sample array for the second note


# Define the frequency and amplitude of a second sine wave
frequency2 = 450
amplitude2 = 5000

# Generate samples for the second sine wave
for i in range(int(sample_rate * duration)):
    sample2 = amplitude2 * np.sin(2 * np.pi * frequency2 * i / sample_rate)
    samples = np.append(samples, sample2)


frequency3 =400
amplitude3 = 5000
for i in range(int(sample_rate * duration2)):
    sample3 = amplitude3 * np.sin(2 * np.pi * frequency3 * i / sample_rate)
    samples = np.append(samples, sample3)

frequency4 =520
amplitude4 = 5000
for i in range(int(sample_rate * duration)):
    sample4 = amplitude4 * np.sin(2 * np.pi * frequency4 * i / sample_rate)
    samples = np.append(samples, sample4)

frequency5 =360
amplitude5 = 5000
for i in range(int(sample_rate * duration)):
    sample5 = amplitude5 * np.sin(2 * np.pi * frequency5* i / sample_rate)
    samples = np.append(samples, sample5)


frequency6 =290
amplitude6 = 5000
for i in range(int(sample_rate * duration2)):
    sample6 = amplitude6 * np.sin(2 * np.pi * frequency6 * i / sample_rate)
    samples = np.append(samples, sample6)

frequency7 =350
amplitude7 = 5000
for i in range(int(sample_rate * duration3)):
    sample7 = amplitude4 * np.sin(2 * np.pi * frequency7 * i / sample_rate)
    samples = np.append(samples, sample7)

frequency8 =500
amplitude8 = 5000
for i in range(int(sample_rate * duration3)):
    sample8 = amplitude8 * np.sin(2 * np.pi * frequency8 * i / sample_rate)
    samples = np.append(samples, sample8)

frequency9 =480
amplitude9 = 5000
for i in range(int(sample_rate * duration3)):
    sample9 = amplitude9 * np.sin(2 * np.pi * frequency9 * i / sample_rate)
    samples = np.append(samples, sample9)

frequency10 =450
amplitude10 = 5000
for i in range(int(sample_rate * duration2)):
    sample10 = amplitude10 * np.sin(2 * np.pi * frequency10 * i / sample_rate)
    samples = np.append(samples, sample10)

frequency11 =350
amplitude11 = 5000
for i in range(int(sample_rate * duration2)):
    sample11 = amplitude11 * np.sin(2 * np.pi * frequency11 * i / sample_rate)
    samples = np.append(samples, sample11)

frequency12 =550
amplitude12 = 5000
for i in range(int(sample_rate * duration)):
    sample12 = amplitude12 * np.sin(2 * np.pi * frequency12 * i / sample_rate)
    samples = np.append(samples, sample12)


frequency13 =690
amplitude13 = 5000
for i in range(int(sample_rate * duration)):
    sample13 = amplitude13 * np.sin(2 * np.pi * frequency13 * i / sample_rate)
    samples = np.append(samples, sample13)


frequency14 =601
amplitude14 = 5000
for i in range(int(sample_rate * duration)):
    sample14 = amplitude14 * np.sin(2 * np.pi * frequency14 * i / sample_rate)
    samples = np.append(samples, sample14)

frequency15 =710
amplitude15 = 5000
for i in range(int(sample_rate * duration)):
    sample15 = amplitude15 * np.sin(2 * np.pi * frequency15 * i / sample_rate)
    samples = np.append(samples, sample15)


frequency16 =750
amplitude16 = 5000
for i in range(int(sample_rate * duration2)):
    sample16 = amplitude16 * np.sin(2 * np.pi * frequency16 * i / sample_rate)
    samples = np.append(samples, sample16)


frequency17 =420
amplitude17 = 5000
for i in range(int(sample_rate * duration2)):
    sample17 = amplitude17 * np.sin(2 * np.pi * frequency17 * i / sample_rate)
    samples = np.append(samples, sample17)

frequency18 =420
amplitude18 = 5000
for i in range(int(sample_rate * duration2)):
    sample18 = amplitude18 * np.sin(2 * np.pi * frequency18 * i / sample_rate)
    samples = np.append(samples, sample18)

frequency19 =450
amplitude19 = 5000
for i in range(int(sample_rate * duration)):
    sample19 = amplitude19 * np.sin(2 * np.pi * frequency19 * i / sample_rate)
    samples = np.append(samples, sample19)

frequency20 =300
amplitude20 = 5000
for i in range(int(sample_rate * duration)):
    sample20 = amplitude20 * np.sin(2 * np.pi * frequency20 * i / sample_rate)
    samples = np.append(samples, sample20)


# Combine the two samples array
combined_sine = samples

# Create a WAV file from the combined samples
with wave.open("combined_sine.wav", "w") as wav_file:
    wav_file.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))
    wav_file.writeframes(samples.astype(np.int16))
