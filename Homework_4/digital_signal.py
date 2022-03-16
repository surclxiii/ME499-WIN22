import numpy as np
import scipy.io.wavfile as wavfile
import scipy.fft as fft


class DigitalSignal(object):
    def __init__(self, data, samp_rate):
        self.sampling_frequency = samp_rate
        self.source_data = data
        self.filtered_data = self.source_data.copy()
        self.freq_low = 0
        self.freq_high = 0.5 * self.sampling_frequency

    @classmethod
    def from_wav(cls, filename):
        """
        Get sample rate and data
        :param filename: (string) name of the file
        :return: data(array), samp_rate(int)
        """
        samp_rate, data = wavfile.read(filename)
        return cls(data, samp_rate)

    def bandpass(self, low=0, high=None):
        """
        Signal processing with bandpass
        :param low: frequency
        :param high: frequency
        :return:
        """
        if high is not None:
            self.freq_high = high
        else:
            self.freq_high = self.sampling_frequency / 2
        t = 1 / self.sampling_frequency
        rfft = fft.rfft(self.source_data)
        fftfreq = fft.rfftfreq(self.source_data.size, t)
        rfft[fftfreq > self.freq_high] = 0
        rfft[fftfreq < low] = 0
        irttf = fft.irfft(rfft)
        self.freq_low = low
        self.filtered_data = np.int16(irttf)

    def subset_signal(self, start=0, end=0):
        """
        Take the data currently in self.filtered_data and subset the signal to only those values whose time values are
        greater than or equal to start and less than or equal to end
        :param start:
        :param end:
        :return:
        """
        subset = []
        time = np.arange(0, self.source_data.size / self.sampling_frequency, step=1/self.sampling_frequency)
        if end == 0:
            end = len(self.source_data) / self.sampling_frequency
        for lists in range(len(time)):
            if start <= time[lists] <= end:
                subset.append(self.filtered_data[lists])
        self.filtered_data = subset
        return self.filtered_data

    def save_wav(self, filename, start=0, end=0):
        """
        Save filtered audio signal
        :param filename: (str) file name
        :param start: (int)
        :param end: (int)
        :return:
        """
        if end == 0:
            end = self.source_data.size / self.sampling_frequency
        wavfile.write(filename, self.sampling_frequency, np.array(self.subset_signal(start, end)))

if __name__ == '__main__':
    buba = DigitalSignal.from_wav('starwars.wav')
    print(buba.sampling_frequency)