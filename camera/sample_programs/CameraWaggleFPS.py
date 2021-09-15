## test for Waggle and nano

from waggle.data.vision import Camera
import time
import cv2

username = 'admin'
password = 'admin'
ip_address = '10.42.0.126'
cam = Camera(f'rtsp://{username}:{password}@{ip_address}:554/cam/realmonitor?channel=1&subtype=1')

## something interesting happens when 'subtype=1' is changed to 'subtype=0'
## give it a try and compare the FPS between the both
## if there's not noticable difference, display the camera stream to the screen with cv2
##   just uncomment the lines below

# setting the calculating variables
frameCount = 500
stop = 0
beg = 0
end = 0

print("Checking FPS and elapsed seconds in capturing", frameCount, "frames")

for sample in cam.stream():
	
#	cv2.imshow('frame', sample.data)
#	if cv2.waitKey(1) & 0xFF == ord('q'):
#        	break

	if (stop == frameCount):
		end = sample.timestamp
		break;
	
	if (stop == 0):
		beg = sample.timestamp

	stop += 1

# cv2.destroyAllWindows()
diff = end - beg
totalTimeSeconds = float(diff / 1e9)

print(f"Total Seconds: ~{totalTimeSeconds}")
print(f"FPS: ~{frameCount / totalTimeSeconds}")
