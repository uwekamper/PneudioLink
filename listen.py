#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import pyaudio
import wave
import os
import sys
import time

from DTMFdetector import DTMFdetector

if len(sys.argv) < 2:
    print("Records a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)
    
# instantiate PyAudio (1)
p = pyaudio.PyAudio()
d = DTMFdetector()
d.reset()

# define callback (2)
def callback(in_data, frame_count, time_info, status):
    print("got framecount %d" % frame_count) 
    #d.goertzel(in_data)
    return (in_data, pyaudio.paContinue)

stream = p.open(format=pyaudio.paInt16, channels=1,rate=44100,input=True,frames_per_buffer=1024) 

stream.read(1024)# wait for stream to finish (5)


# close PyAudio (7)
p.terminate()