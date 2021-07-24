from waggle.data.vision import Camera
from pathlib import Path
import time

cam = Camera(Path("sampleVideo.MP4"))

for sample in cam.stream():
    print(sample.data)