import os
import audioread
import numpy as np

__all__ = ['read']

class Audio:
    def __init__(self, wave, samplerate):
        self._wave = wave
        self._samplerate = samplerate
        self._time = wave.size / samplerate
    
    @property
    def wave(self):
        return self._wave
    
    @property
    def samplerate(self):
        return self._samplerate
    
    @property
    def time(self):
        return self._time

    def __repr__(self):
        return "<Audio [time: {:.2f}s] [samplerate: {:d}]>".format(
            self.time, self.samplerate)

def buf2num(x, n_bytes=2, dtype=np.float32):
    scale = 1./float(1 << ((8 * n_bytes) - 1))
    fmt = '<i{:d}'.format(n_bytes)
    return scale * np.frombuffer(x, fmt).astype(dtype)

def mono(x):
    if x.ndim > 1:
        x = np.mean(x, axis=0)
    return x

def read(path, offset=0.0, dtype=np.float32):
    with audioread.audio_open(os.path.realpath(path)) as audio_file:
        samplerate = audio_file.samplerate
        n_channels = audio_file.channels
        s_start = int(np.round(samplerate * offset)) * n_channels
        s_end = np.inf
        n = 0
        wave = list()
        for frame in audio_file:
            frame = buf2num(frame, dtype=dtype)
            n_prev = n
            n += len(frame)
            if n < s_start:
                # offset is after the current frame
                # keep reading
                continue
            if s_end < n_prev:
                # we're off the end.  stop reading
                break
            if s_end < n:
                # the end is in this frame.  crop.
                frame = frame[:s_end - n_prev]
            if n_prev <= s_start <= n:
                # beginning is in this frame
                frame = frame[(s_start - n_prev):]
            # tack on the current frame
            wave.append(frame)
        
    if wave:
        wave = np.concatenate(wave)
        if n_channels > 1:
            wave = wave.reshape((-1, n_channels)).T
            wave = mono(wave)
    wave = np.ascontiguousarray(wave, dtype=dtype)
    return Audio(wave, samplerate)
