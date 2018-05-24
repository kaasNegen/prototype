from threading import Thread
from real_time_object_detection_single_final import detectObject
import cv2
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time
from pydub import AudioSegment
from pydub.playback import play


class Camera:
    def __init__(self):
        self.dataReady = None
        print("Starting camera")
        self.stream = VideoStream(src=1).start()
        time.sleep(1.0)  # Warm up camera
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        while(True):
            time.sleep(0.1)
            # grab the frame from the threaded video stream and resize it
            # to have a maximum width of 400 pixels
            frame = self.stream.read()
            # Width is 400, length is 300
            frame = imutils.resize(frame, width=400)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # (rows, columns, channels) Channels is the RGB or Gray value
            imageShape = gray.shape
            print("ImageShape")
            print(imageShape)

            brightnessSum = 0
            averageBrightness = 0
            for l in range(0, imageShape[0]):
                for w in range(0, imageShape[1]):
                    brightnessSum += gray[l, w]  # individual pixel

            averageBrightness = brightnessSum / 120000  # 400 * 300
            # Trigger should happen if the brightness is around ~ 100
            print(averageBrightness)

            if averageBrightness < 100:
                self.dataReady = True
                play(AudioSegment.from_mp3(
                    "python-sound-lib/utilAudioFiles/ping.mp3"))
                # Time to remove hand in front of camera and for camera to refocus
                time.sleep(2.0)
                frameToDetect = self.stream.read()
                frameToDetect = imutils.resize(frameToDetect, width=400)
                detectObject(frameToDetect)
                # Wait on this thread for the object detection to finish

    def stop(self):
        self.stream.stop()
        print("Camera stopping")
