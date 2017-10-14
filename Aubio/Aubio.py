#! /usr/bin/env python
import sys, aubio
import demo_bpm_extract as getBmp
import demo_waveform_plot as getWavPlot
import numpy as np

# filePath = "./interval.mp3"
# filePath = "./440_sine.wav"
filePath = "./test.wav"

# return timePointNum-1 "time tag"
timeTagNum = 100

samplerate = 0  # use original source samplerate
hop_size = 256 # number of frames to read in one block

s = aubio.source(filePath, samplerate, hop_size)
total_frames = 0

# Read the wav file stream and find when the audio is started
findStart = True
startFrame = 0
while True: # reading loop
    samples, read = s()

    if(findStart):
        for item in samples:
            # print("item=%f, startFrame=%d " % (item, startFrame))
            startFrame += 1
            if(abs(item) != 0):
                findStart = False

    total_frames += read
    if read < hop_size: break # end of file reached

# Calculate the silence time
silenceTime = startFrame/s.samplerate
# print("The music start at %f s" % (silenceTime))
# print("The music start at frame %d" % (startFrame))
# fmt_string = "read {:d} frames at {:d}Hz from {:s}"
# print (fmt_string.format(total_frames, s.samplerate,filePath ))


# get the bmp of music to calculate where should add a time point

bmp = getBmp.get_file_bpm(filePath)
if(bmp <= 0):
    print("Bad music which contains no tempo")
    # Only when the music contains tempo infomation then go further
    sys.exit(0)

bmp_Second = 60/bmp
endTime = total_frames/s.samplerate
startTime = 0.
totalBar = endTime/bmp_Second

interval = bmp_Second*round(totalBar/timeTagNum)
tagTimePoint = np.arange(startTime+silenceTime,endTime,interval)

# print("File BMP is %f"%(bmp))
# print("Total time is %f"%(endTime))
# print("Total bar is %f"%(totalBar))

print("Time tags are:\n")
print(tagTimePoint)

getWavPlot.get_waveform_plot(filePath)
import matplotlib.pyplot as plt
plt.show()

