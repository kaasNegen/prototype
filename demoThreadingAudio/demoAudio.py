from pydub import AudioSegment
from pydub.playback import play
import time
from threading import Thread

def playAudioFromObjectDetection():
    play(AudioSegment.from_mp3("./demoThreadingAudio/car.mp3"))


class Camera:
    def __init__(self):
        print("Starting camera")
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        while True:
            time.sleep(0.1)
            play(AudioSegment.from_mp3("./demoThreadingAudio/ping.mp3"))

    def stop(self):
        self.stream.stop()
        print("Camera stopping")


Camera()
playAudioFromObjectDetection()
time.sleep(0.5)
playAudioFromObjectDetection()