import pyaudio
import wave

class audio:
    def __init__(self,RECORD_TIME):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 512
        self.RECORD_SECONDS = RECORD_TIME
        self.WAVE_OUTPUT_FILENAME = "file.wav"     
        self.audio = pyaudio.PyAudio()
        self.frames = []
    #start Recording
        print('test')
    
    def run(self):
        print('run')
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                rate=self.RATE, input=True,
                frames_per_buffer=self.CHUNK)
                #print("recording...")
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            #print("finished recording")
        #stop Recording
        stream.stop_stream()
        stream.close()
        self.audio.terminate()
        #Save File 
        waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(self.frames))
        waveFile.close()