import pylab as pl
import matplotlib
from scipy.io import wavfile

sampFreq, snd = wavfile.read('LittleStar.wav')
print snd.dtype
snd = snd / (2.**15)
print snd.shape

s1 = snd[:,0]

timeArray = pl.arange(0, 1130496, 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds

pl.plot(timeArray, s1, color='k')
pl.ylabel('Amplitude')
pl.xlabel('Time (ms)')
pl.show()
