<h1>Microphone</h1>

This directory contains instructions on how to set up the microphone with the Jetson Nano along with some example code.

---

<h2>Reference</h2>

<h3>Recording Audio:</h3>

Required Libraries:
```
import sounddevice as sd
from scipy.io.wavfile import write
```

Set Sample Frequency and Duration:
```
freq = 44100
duration = 5
```

Record:
```
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()
```

Convert to WAV File:
```
write("recording.wav", freq, recording)
```

<h3>Reading WAV Files</h3>

Required Libraries:
```
from scipy.io import wavfile
import scipy.io
```

Read in WAV File:
```
(samplerate, data) = wavfile.read('recording.wav')
```

---

<h2>Directory Contents:</h2>

<h2>readingWavFiles.ipynb</h2>

* Instructions and code demonstrating how to read WAV files into a Python program

<h2>recordingWavFiles.ipynb</h2>

* Instructions and code demonstrating how to record WAV files in a Python program using the microphone

<h2>sample.wav</h2>

* A sample WAV file for use in the `readingWavFiles` notebook

<h2>readme.md</h2>

* This file
