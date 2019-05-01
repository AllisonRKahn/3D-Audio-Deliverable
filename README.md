# 3D Audio Python Example

## Pre-request

To run the code in this demo, you need following libraries installed

* `portaudio` (cross platform audio backend, written in C)
    * [Windows Installation](https://python-forum.io/Thread-portaudio-installation-on-windows-10)
    * Mac: Use [Homebrew](https://brew.sh/)
    * Linux: you can install it with any package manager(apt, snap, yum etc.)
* Python related packages, should be installed after portaudio being installed. You can install all these modules through `pip`
    * `pyaudio`
    * `sounddevice`
    * `pygame`


## To Run GUI
The GUI is just run with 
```shell
python finalGUI.py
```
This file calls `Audiotemp.py` and `spatializer_demo.py` to play the audio. This file also connects to the seperate localization file via a socket. 

### The GUI uses the python libraries time, math, socket, json, numpy and OS

To install these libraries type 
```shell
pip install ___
```
In order to use the localizers, after clicking on the 'use marvelmind' code, in another window open `example.py` inside the read-gyro-and-location folder. This find also uses the time, sys, numpy, math and socket libraries with can also be installed with pip.

### In order to play audio from the GUI, you must also have the dependencies for the `spatializer_demo.py` file

These libraries include scipy, numpy, math, time, multiprocessing and playback as detailed above. This file also uses `playback.py` which requires time, enum, pygame, sounddevice, and pyaudio as well detailed above.

## For Information on beginning the MarvelMind Locators, please reference the readme in the `marvelmind-position-and-angle` folder


## Setup

`setup.sh` is an included setup file for use on Raspberry Pi's. 

### On Raspberry Pi

In the terminal run
```shell
chmod u+x setup.sh
./setup.sh
```

Installs the following libraries
* numpy
* scipy
* sounddevice
* portaudio (necessary for sounddevice to work properly)

## Running the Demo

For the demo, in the terminal of your machine run the following
```shell
python3 spatializer_pi.py
```


## Files in the repo

* `playback.py` is a backend Adapter, it can help you to choose using which python audio backend for playback
* `test_playback.py` is a simple demo for how to use all these backends to play a generated signal(sine wave) in buffer.
* `spatializer_demo.py` is a translation for the demo in 3D audio class. The demo read a wave file, and synthesize the signal with a CIPIC HRTF file(in MATLAB format); then generates an audio buffer; finally play the buffer use the backend in playback.py
* `spatializer.py` refactoring of spatialization demo that implements a buffer
* `spatializer_pi.py` is the same as `spatializer_pi.py` but is in `Python 3.5` so it can be run on a Raspberry Pi
* `finalGUI.py` is the file that contains the GUI and calls the localization and audio code
* `Audiotemp.py` is a helper file for the GUI that calculates the index for audio that is played on `spatializer_demo.py`

## Bugs
