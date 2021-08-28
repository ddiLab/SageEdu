from waggle.data.audio import Microphone
from scipy.io import wavfile
import numpy as np
import time
import sys
from colorama import Fore, Back, Style

microphone = Microphone()

def time_ns():
    return int(time.time() * 1e9)

def getAudioSample(duration, sample_name):
    sample = microphone.record(sample_time)
    sample.save(f"collected_data/audio_samples/{sample_name}")
    (samplerate, data) = wavfile.read(f'collected_data/audio_samples/{sample_name}')
    return data

# Script Arguments
sample_delay = int(sys.argv[1]) # Time between each sample - (seconds)
sample_time  = int(sys.argv[2]) # Duration of each sample -- (seconds)
run_time     = int(sys.argv[3]) # Total Run Time ----------- (minutes)
file_name    = str('collected_data/' + sys.argv[4]) # File name to save data

# Number of seconds data has been collected
live_time = 0

# A 2D array where the collected data will be stored
# First entry contains metadata
data = [[time_ns(), sample_delay, sample_time, run_time]]

print(Back.GREEN +
      'Collecting data for ' + str(run_time) + ' mins with ' + 
      str(sample_time) + ' sec samples at ' +
      str(sample_delay) + ' sec intervals' +
      Style.RESET_ALL)

while live_time < (run_time + 1) * 60:
    startTime = time_ns()
    sample_name = 'sample_' + str(startTime) + '.wav'
    sample = getAudioSample(sample_time, sample_name)
    avgAmp = np.average(np.absolute(sample))
    maxAmp = np.amax(np.absolute(sample))
    minAmp = np.amin(np.absolute(sample))

    data = np.append(data, [[startTime,
                             avgAmp,
                             maxAmp,
                             minAmp]], axis=0)

    print('Sample collected at ' + str(startTime) + ' seconds')

    # Increments the number of minutes data has been collected
    live_time += sample_time + sample_delay

    if live_time < (run_time + 1) * 60:
        # Waits sample_delay seconds before going back to the beginning of the
        # loop and taking the next measurement
        time.sleep(sample_delay)

np.savetxt(file_name, 
           data,
           delimiter=",",
           fmt='%1.3f')

print(Back.GREEN +
    'Saved data to ' + file_name +
    Style.RESET_ALL)
