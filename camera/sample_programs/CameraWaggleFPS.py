## test for Waggle and nano

from waggle.data.vision import Camera
import time

cam = Camera('rtsp://admin:admin@10.42.0.127:554/cam/realmonitor?channel=1&subtype=0')

frameCount = 500
stop = 0
beg = 0
end = 0

for sample in cam.stream():
	if (stop == frameCount):
		end = sample.timestamp
		break;
	
	if (stop == 0):
		beg = sample.timestamp

	stop += 1

diff = end - beg
totalTimeSeconds = float(diff / 1e9)

print(f"Total Seconds: {totalTimeSeconds}")
print(f"FPS: {frameCount / totalTimeSeconds}")
