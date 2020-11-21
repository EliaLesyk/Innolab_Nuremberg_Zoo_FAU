from flask import render_template, Flask, Response, stream_with_context
from video import VideoFile


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


def gen(video):
    while True:
        #get video frame
        frame = video.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(stream_with_context(gen(VideoFile())), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()