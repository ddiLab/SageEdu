from waggle.data.audio import Microphone
from scipy.io import wavfile
import numpy as np
import time
import sys
from colorama import Fore, Back, Style

microphone = Microphone()
start_time = time.time()

def time_ns():
    return int(time.time() * 1e9)

def getAudioSample(duration, sample_name):
    sample = microphone.record(sample_time)
    sample.save(f"collected_data/audio_samples/{sample_name}") 
    (samplerate, data) = wavfile.read(f'collected_data/audio_samples/{sample_name}') 
    return data

def calculate_run_time(delay, duration, max_time):
    combined = delay + duration
    sections = max_time // combined
    lost_time = max_time % combined
    run_time = round((max_time - lost_time) / 60, 2)
    return sections, run_time

# Script Arguments
sample_delay = int(sys.argv[1]) # Time between each sample - (seconds)
sample_time  = int(sys.argv[2]) # Duration of each sample -- (seconds)
max_time     = int(sys.argv[3]) # Max Run Time ----------- (minutes)
file_name    = str('collected_data/' + sys.argv[4]) # File name to save data


# calculates the actual run time to eliminate going over the max run time
sections, run_time = calculate_run_time(sample_delay, sample_time, max_time*60)

# A 2D array where the collected data will be stored
# First entry contains metadata
data = [[time_ns(), sample_delay, sample_time, run_time]]


print(Back.GREEN +
      'Collecting audio for approx. ' + str(run_time) + ' mins with ' + 
      str(sample_time) + ' sec samples at ' +
      str(sample_delay) + ' sec intervals' +
      Style.RESET_ALL)


for x in range(sections):
    combined_time = (time.time() - start_time) + sample_delay + sample_time
    if (combined_time > max_time*60):
        break

    timestamp = time_ns()
    sample_name = 'sample_' + str(timestamp) + '.wav'
    sample = getAudioSample(sample_time, sample_name)
    avgAmp = np.average(np.absolute(sample))
    maxAmp = np.amax(np.absolute(sample))
    minAmp = np.amin(np.absolute(sample))

    data = np.append(data, [[timestamp,
                             avgAmp,
                             maxAmp,
                             minAmp]], axis=0)

    print('Sample collected at ' + str(timestamp) + ' nanoseconds')

    time.sleep(sample_delay)


np.savetxt(file_name, 
           data,
           delimiter=",",
           fmt='%1.3f')

print(Back.GREEN +
    'Saved data to ' + file_name +
    Style.RESET_ALL)
