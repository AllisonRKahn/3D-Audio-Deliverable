import scipy
from scipy.io import wavfile, loadmat
import numpy as np
import math
import time
import playback as pb
from typing import Dict,List

BUFFER_SIZE:        int = 2048*2
E_INDEX    :        int = 16
DB_DATA    :       dict = loadmat('./CIPIC_58_HRTF.mat')
FREQ       :        int = None
SIG_DATA   : np.ndarray = None
    
AZIMUTHS   :  List[int] = [
    -80, -65, -55, -45, -40,
    -35, -30, -25, -20, -15,
    -10,  -5,   0,   5,  10, 
     15,  20,  25,  30,  35, 
     40,  45,  55,  65,  80,
]

FREQ,SIG_DATA = wavfile.read('./RiverStreamAdjusted.wav')

SIG_DATA = SIG_DATA/2**15
SIG_DATA = np.concatenate((SIG_DATA,SIG_DATA),axis=None)

temp_buffer = None
buffer      = None
temp_l      = None
temp_r      = None
reverse     = False

if __name__ == '__main__':
    increments: List[int] = range(0,len(SIG_DATA)//BUFFER_SIZE)
    index     :       int = 0
    a_index   :       int = 0

    while index < len(increments):
        buffer_in: List[float] = SIG_DATA[
            BUFFER_SIZE * increments[index] : BUFFER_SIZE * (increments[index] + 1)
        ]

        left : np.ndarray = np.squeeze(DB_DATA['hrir_l'][a_index, E_INDEX, :])
        right: np.ndarray = np.squeeze(DB_DATA['hrir_r'][a_index, E_INDEX, :])
        delay: np.float64 = DB_DATA['ITD'][a_index, E_INDEX]
        zeros: np.ndarray = np.zeros(int(math.floor(abs(delay))))

        if a_index < 12:
            left  = np.append(left , zeros)
            right = np.append(zeros, right)
        else:
            left  = np.append(zeros,  left)
            right = np.append(right, zeros)

        wav_l = np.convolve(left , buffer_in)
        wav_r = np.convolve(right, buffer_in)

        a_index += 1
        index   += 1
        
        if a_index is 0:
            reverse = False
            E_INDEX = 16

        if a_index == len(AZIMUTHS):
            reverse = True
            E_INDEX = 0
        
        if reverse:
            a_index -= 2
            
        if temp_l is None:
            temp_l = wav_l
        else:
            temp_l = np.concatenate((temp_l,wav_l),axis=None)
        
        if temp_r is None:
            temp_r = wav_r
        else:
            temp_r = np.concatenate((temp_r,wav_r),axis=None)
        
    temp_buffer = np.vstack((temp_l,temp_r))
    buffer = np.transpose(temp_buffer)

    player: pb.Playback = pb.Playback(pb.Backend.SOUNDDEVICE)
    player.play(freq=FREQ, buffer=buffer, channel=2, play_time=len(buffer)/FREQ)
    # write wav
