from webcamvideostream import WebcamVideoStream

class VideoStream:
    def __init__(self, src=0, usePiCamera=False, resolution=(320, 240), framerate=32):
        if (usePiCamera):
            from pivideostream import PiVideoStream
            self.stream = PiVideoStream(resolution=resolution, framerate=framerate)
        else:
            self.stream = WebCamVideoStream(src=src)
    
    def start(self):
        return self.stream.start()
    
    def update(self):
        return self.stream.update()
    
    def read(self):
        return self.stream.read()
    
    def stop(self):
        return self.stream.stop()