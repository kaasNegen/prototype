from audio.audio import *
# from detectionfields.detectionfields import *
from camera.camera import *

audioService = Audio()
cameraService = Camera()

audioService.start()
while(True):
    time.sleep(0.1)
    # if cameraService.data_ready:
    #     for thing in cameraService.data_ready:
    #         (name, pan_value) = thing
    #         audioService.playSample(name, pan_value)
        # cameraService.data_ready = None
