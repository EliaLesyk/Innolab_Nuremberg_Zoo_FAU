from picamera import PiCamera
from time import sleep


class Cam:
    def __init__(self):
        self._running = True
        self.camera = PiCamera()
        self.camera.resolution=(1280,780)

    def terminate(self):
        self._running = False
        self.camera.stop_recording()
        self.camera.stop_preview()
        self.camera.close()

    def run(self):
        self.camera.start_preview(fullscreen=False, window=(10,0,320,240))
        self.camera.start_recording('/home/pi/Documents/MultiThreadingVideo.h264')
        while self._running:
            self.camera.wait_recording(1)