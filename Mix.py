import echonest.remix.audio as audio

# Easy around wrapper mp3 decoding and Echo Nest analysis
audio_file = audio.LocalAudioFile("440_sine.wav")

# You can manipulate the beats in a song as a native python list
beats = audio_file.analysis.beats

print(beats)