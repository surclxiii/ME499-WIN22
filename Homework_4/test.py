import numpy as np
from scipy.io import wavfile
from scipy import fft

class DigitalSignal:
    def __init__(self, arr, sampling_freq):
        self.source_data = arr
        self.sampling_frequency = sampling_freq
        self.filtered_data = arr.copy()
        self.freq_low = 0
        self.freq_high = 0.5*int(sampling_freq)
        # print(self.sampling_frequency)
        # print(self.freq_high)
        # print(type(self.source_data[0]))
    @classmethod
    def from_wav(cls, f_name):
        rate, data = wavfile.read(f_name)
        # print(rate)
        # print(data)
        return cls(data, rate)

    def bandpass(self, low=0, high=None):
        if high is not None:
            self.freq_high = high
        else:
            self.freq_high = self.sampling_frequency/2
        T = 1 / self.sampling_frequency
        tf = fft.rfft(self.source_data)
        tf_freq = fft.rfftfreq(self.source_data.size, T)
        tf[tf_freq > self.freq_high] = 0
        tf[tf_freq < low] = 0
        itf = fft.irfft(tf)
        self.filtered_data = np.int16(itf)
        self.freq_low = low

    def subset_signal(self, start=0, end=0):
        if end == 0:
            end = len(self.source_data)/self.sampling_frequency
        subset = []
        time = np.arange(0, self.source_data.size/self.sampling_frequency, step=1/self.sampling_frequency)
        for lists in range(len(time)):
            if start <= time[lists] <= end:
                subset.append(self.filtered_data[lists])
        self.filtered_data = subset
        print(type(self.filtered_data))
        return self.filtered_data

    def save_wav(self, filename, start=0, end=0):
        if end == 0:
            end = self.source_data.size/self.sampling_frequency
        wavfile.write(filename, self.sampling_frequency , np.array(self.subset_signal(start, end)))
        # print(self.source_data)
        # print(self.filtered_data)
        # print(range(end))


if __name__ == '__main__':

    wave = DigitalSignal.from_wav(f_name='sinewave1000hz.wav')
    wave.bandpass()
    wave.subset_signal(0,10)
    wave.save_wav("try")
