# Microphone Sample Programs

This directory contains basic programs that make use of the microphone.

---

## Directory Contents:


### [CameraAudioWaggle.py](https://github.com/ddiLab/SageEdu/blob/dev/microphone/sample_programs/CameraAudioWaggle.py)
* Python program that is able to save just video footage without any audio from the camera into the current directory using the Waggle platform
* There are comments outlining possible methods of also including audio, but errors arise when using ffmpeg's libx264 with opencv
* The error might be fixable by changing some .config files of opencv
