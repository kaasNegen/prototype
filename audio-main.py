from audio.Audio import *
from detectionfields.detectionfields import *
from Camera import *

audio = Audio()
camera = Camera()

audio.start()
while(True):
    audio.emit(500, 0.5)
    time.sleep(2)
    audio.stop()
    time.sleep(2)
    audio.start()
    time.sleep(2)




