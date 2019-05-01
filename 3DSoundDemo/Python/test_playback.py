"""
https://www.scivision.co/playing-sounds-from-numpy-arrays-in-python/
"""
import numpy as np
import playback


def main():
    freq = 8000  # Hz
    TIME = 1.  # second, arbitrary length of tone

    # 1 kHz sine wave, 1 second long, sampled at 8 kHz
    t = np.arange(0, TIME, 1/freq)
    # 0.5 is arbitrary to avoid clipping sound card DAC
    x = 0.5 * np.sin(2*np.pi*1000*t)
    # scale to int16 for sound card. SoundDevice can skip this step
    x = (x*(2**15)).astype(np.int16)

    # pb = playback.Playback(playback.Backend.SOUNDDEVICE)
    # pb = playback.Playback(playback.Backend.PYAUDIO)
    pb = playback.Playback(playback.Backend.PYGAME)
    pb.play(freq=freq, buffer=x, play_time=TIME)


if __name__ == '__main__':
    main()
