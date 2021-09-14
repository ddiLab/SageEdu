# helper program for StreamWithThreading.ipynb

from threading import Thread
import cv2
class ThreadedStream:
	def __init__(self, src='rtsp://admin:admin@10.42.0.126:554/cam/realmonitor?channel=1&subtype=0'):
		# initialize the video camera stream and read the first frame
		self.stream = cv2.VideoCapture(src)
		(self.grab, self.frame) = self.stream.read()

	def start(self):
		# start the thread to read frames from the video stream
		Thread(target=self.update, args=()).start()
		return self

	def update(self):
		# keep looping infinitely until the process is stopped
		while True:
			(self.grabbed, self.frame) = self.stream.read()

	def read(self):
		# return the frame most recently read
		return self.frame
