import sounddevice
from scipy.io.wavfile import write
fs= 44100       #sample rate
second= int(input('Enter the time duration in second: '))
print('Recording.....\n')
record_voice=sounddevice.rec(int(second * fs), samplerate=fs,channels=2)
sounddevice.wait()
write('out1.wav',fs,record_voice)
print('Finished.....\nPlease check it....')

# working but voice not recorded in that file_07/12/22
