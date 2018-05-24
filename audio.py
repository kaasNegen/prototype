from pyo import *

class Audio:
    
    def __init__(self):
        self.server = Server(sr=48000, buffersize=512, duplex=0, winhost="asio")
        self.server.boot()
        self.lfo = LFO(freq=0)
        self.pan = Pan(self.lfo, spread=0)

    def emit(self, frequency, angle):
        if(self.STATE == 'RUNNING'):
            self.lfo.setFreq(frequency)
            self.pan.setPan(angle)

    def stop(self):
        self.server.stop()
        self.STATE = 'PAUSED'

    def start(self):
        self.server.start()
        self.STATE = 'RUNNING'




