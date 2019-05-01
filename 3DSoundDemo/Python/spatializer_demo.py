import scipy
from scipy.io import wavfile, loadmat
import numpy as np
import math
import time
import playback as pb
import multiprocessing

#finds the HRTFs and actually plays the audio

def play(playFromThisPoint):
    # 25 azimuth degrees
    azimuths = [-80, -65, -55, -45, -40, -35, -30, -25, -20,
                -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 65, 80]

    # 50 elevation degrees
    elevations = [-45+5.625*e for e in range(50)]
    # freq, sig_data = wavfile.read('./RiverStreamAdjusted.wav')
    freq, sig_data = wavfile.read('./RiverStreamAdjusted.wav')
    sig_data = sig_data / 2**15  # from int16(16 bits) scale to -1 to 1
    #print("data size: {},freq: {}".format(len(sig_data), freq))
    db_data = loadmat('./CIPIC_58_HRTF.mat')
    aIndex = int(playFromThisPoint)
    eIndex = 16

    left = np.squeeze(db_data['hrir_l'][aIndex, eIndex, :])  # 200*1
    right = np.squeeze(db_data['hrir_r'][aIndex, eIndex, :])  # 200*1

    delay = db_data['ITD'][aIndex, eIndex]  # float
    hrir_zeros = np.zeros(math.floor(abs(delay)))
    #print(type(hrir_zeros))

    if aIndex < 12:
        left = np.append(left, hrir_zeros)
        right = np.append(hrir_zeros, right)
    else:
        left = np.append(hrir_zeros, left)
        right = np.append(right, hrir_zeros)

    wave_left = np.convolve(left, sig_data)
    wave_right = np.convolve(right, sig_data)
    buffer = np.vstack((wave_left, wave_right))
    buffer = np.transpose(buffer)

    # choose a playback backend
    print("Playing sound")

    player = pb.Playback(pb.Backend.SOUNDDEVICE)
    #print("~~~~~~")
    #print(freq)
    #print(buffer)


    player.play(freq=freq, buffer=buffer, channel=2) 
    time.sleep(1)


#used to test if file is working
#plays audio in a circle with 2 seconds at each point
if __name__ == '__main__':

    arrayToUse = range(0,24)
    for i in arrayToUse:

        p = multiprocessing.Process(target=play, args=(str(i),))
        p.start()
        p.join(2)
        if p.is_alive():
            p.terminate()
            p.join()
