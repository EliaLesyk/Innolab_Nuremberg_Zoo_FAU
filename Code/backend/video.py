import cv2 as cv


class VideoFile:
    def __init__(self):
        # Source here static video, but could also be a camera
        self.video = cv.VideoCapture('static/video_example.mp4')
        self.last_frame = None

    def __del__(self):
        # releasing video
        self.video.release()

    def get_frame(self):
        # extracting frames
        ret, frame = self.video.read()
        # if frame is read correctly ret is True
        if not ret:
            print("no frame anymore, start from the beginning")
            self.video.set(cv.CAP_PROP_POS_FRAMES, 0)
            return self.last_frame
        ret, jpeg = cv.imencode('.jpg', frame)
        self.last_frame = jpeg.tobytes()
        return jpeg.tobytes()
