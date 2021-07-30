from waggle.data.audio import Microphone
import time

from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

import bme680

microphone = Microphone()

sensor = bme680.BME680()
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.DISABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

micAC = False
enviAC = False
enviData = []

print("Calibrating Microphone...")
sample = microphone.record(10)
sample.save("ACDetector.wav")
(samplerate, data) = wavfile.read('ACDetector.wav')
noAC = np.average(np.absolute(data))

print("Calibrating Envi Sensor...")
temp = []
for i in range(1, 10):
    if sensor.get_sensor_data():
        temp.append(sensor.data.temperature)
    
    time.sleep(1)

norm_temp = np.average(temp)


print("Running...")
while True:
    # Recording Audio
    sample = microphone.record(10)
    sample.save("ACDetector.wav")
    (samplerate, data) = wavfile.read('ACDetector.wav')

    avgAmp = np.average( np.absolute(data))

    # Check if AC is on based on sound
    if (avgAmp - noAC > 5) and not micAC:
        print("AC is now on based on mic")
        micAC = True  
    elif micAC:
        print("AC is now off based on mic")
        micAC = False

    for i in range(1,10):
        if sensor.get_sensor_data():
            reading = [sensor.data.temperature,
                       sensor.data.pressure,
                       sensor.data.humidity]

            enviData = np.append(enviData, [reading], axis=0)

    avgTemp = np.average(enviData)
    # Check if AC is on based on temperature
    if (norm_temp - avgTemp > 5) and not enviAC:
        print("AC is now on based on envi")
        enviAC = True  
    elif enviAC:
        print("AC is now off based on envi")
        enviAC = False

    time.sleep(10)