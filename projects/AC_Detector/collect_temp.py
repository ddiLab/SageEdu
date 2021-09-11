"""
This script takes readings of humidity, air pressure, temperature,
and gas resistance and saves it to a file.
"""

# Required Libraries
import bme680
import time
import numpy as np
import sys
from colorama import Fore, Back, Style

start_time = time.time()

# Sensor Setup
sensor = bme680.BME680()

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

def time_ns():
    return int(time.time() * 1e9)

def get_temp():
    if sensor.get_sensor_data():
        if sensor.data.heat_stable:
            # Returns a reading of temperature with the timestamp
            return [time_ns(), sensor.data.temperature]
        else:
            # Gas resistance reading cannot be taken; doesn't affect temperature readings
            return [time_ns(), sensor.data.temperature]
    else:
        # No data is available
        return [time_ns(), None]

def calculate_run_time(delay, max_time):
    sections = max_time // delay
    lost_time = max_time % delay
    run_time = round((max_time - lost_time) / 60, 2)
    return sections, run_time

# Script Arguments
run_delay  = int(sys.argv[1]) # Time between each measurment ------ (seconds)
max_time   = int(sys.argv[2]) # Max run time -------------------- (minutes)
file_name  = str('collected_data/' + sys.argv[3]) # File name to save data


# calculates the actual run time to eliminate going over the max run time
sections, run_time = calculate_run_time(run_delay, max_time*60)

# A 2D array where the collected data will be stored
#  first entry contains metadata
data = [[run_delay, run_time]]

print(Back.GREEN +
      'Collecting temp for approx. ' + str(run_time) + ' mins at ' +
      str(run_delay) + ' sec intervals' +
      Style.RESET_ALL)

x = 0
while x < sections:
    combined_time = (time.time() - start_time) + run_delay
    if (combined_time > max_time*60):
        break

    reading = get_temp() # for some reason the first reading never works

    if reading[1] == None:
        # No data is available
        print(Fore.YELLOW +
              'Warning: No data could be collected at ' +
              str(reading[0]) + ' nanoseconds' +
              Style.RESET_ALL)
        continue
    else:            
        # The array with the last set of readings is added to
        # the 2D array containing all the data
        data = np.append(data, [reading], axis=0)
            
        print('Data collected at ' + str(reading[0]) + ' nanoseconds') 

    # sleeps for an amount of specified seconds
    time.sleep(run_delay)
    x += 1

# Save all the data that was collected and stored in the data array to a file
np.savetxt(file_name, 
           data,
           delimiter=",",
           fmt='%1.3f')

print(Back.GREEN +
      'Saved data to ' + file_name +
      Style.RESET_ALL)
