## test for Waggle and nano

from waggle.data.vision import Camera, BGR
import time
import cv2

cam = Camera('rtsp://admin:admin@10.42.0.126:554/cam/realmonitor?channel=1&subtype=1', BGR)

frameCount = 1000
stop = 0
beg = 0
end = 0
#### Using python packages has not worked when capturing audio from the camera/saving a video with audio from the camera 
fourcc = cv2.VideoWriter_fourcc(*'MJPG') # codec should be X264 for saving mp4 file
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (704, 480)) # only saves video without audio

for sample in cam.stream():
    if (stop == frameCount):
        end = sample.timestamp
        break

    # hsv = cv2.cvtColor(sample.data, cv2.COLOR_BGR2HSV)
    # out.write(hsv)
    out.write(sample.data)
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL) resize window, but it leads to more lag and is glitchy
    # cv2.resizeWindow('image', 2000, 2000)
    cv2.imshow('image', sample.data)
    # cv2.imshow('hsv', hsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        end = sample.timestamp
        break
        
    if (stop == 0):
        beg = sample.timestamp
        
    stop += 1

out.release()
print(f"Beg: {beg}")
print(f"End: {end}")
diff = end - beg
totalTimeSeconds = float(diff / 1e9)

print(f"Total Seconds: {totalTimeSeconds}")
print(f"FPS: {stop / totalTimeSeconds}")
