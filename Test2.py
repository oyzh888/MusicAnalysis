#required libraries
import urllib
import scipy.io.wavfile
import pydub

rate,audData=scipy.io.wavfile.read("440_sine.wav")

print(rate)
print(audData)
print(audData.shape)
print(audData.shape[0])
print(audData.shape[0]/rate)

channel1=audData[:,0] #left
channel2=audData[:,1] #right

i = 0
for index,item in enumerate(channel1) :
    print(item)
    i+=1
    # if(i>100): break


print("Len is")
print(i)

import numpy as np
#averaging the channels damages the music
mono=np.sum(audData.astype(float), axis=1)/2

import matplotlib.pyplot as plt

#create a time variable in seconds
time = np.arange(0, float(audData.shape[0]), 1) / rate

#plot amplitude (or loudness) over time
# plt.figure(1)
# plt.subplot(211)
# plt.plot(time, channel1, linewidth=0.01, alpha=0.7, color='#ff7f00')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.subplot(212)
# plt.plot(time, channel2, linewidth=0.01, alpha=0.7, color='#ff7f00')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.show()

