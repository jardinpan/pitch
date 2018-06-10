import numpy as np
import matplotlib.pyplot as plt

__all__ = ['track']

freqs_metadata = list(440 * np.array([2**(k/12) for k in range(12)]))
pitch_metadata = ['A3', '#A3', 'B3', 'C4', '#C4', 'D4', '#D4', 'E4', 'F4', '#F4', 'G4', '#G4', 'A4']

class TrackData:
    def __init__(self, audio, freq, tracking):
        self._audio = audio
        self._freq = freq
        self._tracking = tracking
    
    @property
    def audio(self):
        return self._audio

    @property
    def freq(self):
        return self._freq
    
    @property
    def tracking(self):
        return self._tracking
    
    def visualize(self):
        plt.plot(np.linspace(0, self.audio.time, self.tracking.size), self.tracking)
        plt.grid()
        plt.yticks(freqs_metadata, pitch_metadata)
        plt.xlabel('Time (s)')
        plt.ylabel('Pitch')
        plt.title('Pitch Tracking')
        plt.show()
    
    def spectrum(self, max_freq=4000,):
        plt.specgram(self.audio.wave, Fs=self.audio.samplerate, NFFT=1024)
        plt.ylim(0, max_freq)
        plt.xlabel('Time (s)')
        plt.ylabel('Spectrum')
        plt.title('Spectrum (STFT)')
        plt.show()


def track(audio, window=np.hanning, scale=0.1, max_freq=4000, threshold=7.0):
    """STFT"""
    n = int(scale * audio.samplerate)  # Signal length
    m = int(audio.wave.size / n)  # Time length
    reso = audio.samplerate / (n-1)  # Resolution
    freq = [reso * k for k in range(n) if reso * k <= max_freq]
    d = len(freq)
    tracking = np.zeros(m)
    for j in range(m):
        fft_data = np.fft.fft(window(n) * audio.wave[n*j:n*(j+1)]) * 2 / n
        abs_fft_data = abs(fft_data)[:d]
        if energy(audio.wave[n*j:n*(j+1)]) < threshold:
            tracking[j] = tracking[j-1]
        else:
            tracking[j] = freq[np.where(abs_fft_data==np.max(abs_fft_data))[0][0]]
    return TrackData(audio, freq, tracking)

def energy(frame):
    return np.linalg.norm(frame, 2)
