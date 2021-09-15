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

def get_all_readings():
    if sensor.get_sensor_data():
        if sensor.data.heat_stable:
            # Takes a reading of everything and stores it in an array
            reading = [sensor.data.temperature,
                       sensor.data.pressure,
                       sensor.data.humidity,
                       sensor.data.gas_resistance]
        else:
            # Gas resistance reading cannot be taken
            reading = [sensor.data.temperature,
                       sensor.data.pressure,
                       sensor.data.humidity,
                       -1]

        return [time_ns(), reading]
        
    else:
        # No data is available
        return [time_ns(), None]

def calculate_run_time(delay, max_time):
    if (delay == 0):
        return max_time*60, max_time//60

    sections = max_time // delay
    lost_time = max_time % delay
    run_time = round((max_time - lost_time) / 60, 2)

    return sections, run_time

# Script Arguments
burn_delay = int(sys.argv[1]) # Time between each burn-in reading - (seconds)
max_burn_time  = int(sys.argv[2]) # Max burn-in time ---------------- (minutes)
run_delay  = int(sys.argv[3]) # Time between each measurment ------ (seconds)
max_time   = int(sys.argv[4]) # Max run time -------------------- (minutes)
file_name  = str("collected_data/" + sys.argv[5]) # File name to save data

burn_sections, burn_run_time = calculate_run_time(burn_delay, max_burn_time*60)
sections, run_time = calculate_run_time(run_delay, max_time*60)

# A 2D array where the collected data will be stored
# First entry contains metadata
data = [[burn_delay, burn_run_time, run_delay, run_time, 0]]

# Sensor burn in
print(Back.GREEN +
      'Burnning in for ~' + str(burn_run_time) + ' mins at ' +
      str(burn_delay) + ' sec intervals' +
      Style.RESET_ALL)

burn_start = time.time()
num = 0
while num < burn_sections:
    burn_combined_time = (time.time() - burn_start) + burn_delay
    if (burn_combined_time > max_burn_time*60):
        break

    get_all_readings()
    time.sleep(burn_delay)
    num += 1


# Collection of data   
print(Back.GREEN +
      'Collecting data for ~' + str(run_time) + ' mins at ' +
      str(run_delay) + ' sec intervals' +
      Style.RESET_ALL)

start = time.time()
num = 0
while num < sections:
    combined_time = (time.time() - start) + run_delay
    if (combined_time > max_time*60):
        break 

    result  = get_all_readings()

    if result[1] == None:
        # No data is available
        print(Fore.YELLOW +
              'Warning: No data could be collected at ' +
              str(time_ns()) + ' nanoseconds' +
              Style.RESET_ALL)
        continue
    else:
        if result[1][3] == -1:
            print(Fore.YELLOW +
                    'Warning: Gas resistance data could not be collected at ' +
                    str(time_ns()) + ' nanoseconds' +
                    Style.RESET_ALL)
        else:
            # The array with the last set of readings (result[1]) is added to
            # the 2D array containing all the data
            data = np.append(data, [[result[0],
                                     result[1][0],
                                     result[1][1],
                                     result[1][2], 
                                     result[1][3]]], axis=0)
            
            print('Data collected at ' + str(time_ns()) + ' nanoseconds') 
        
    # sleeps for an amount of specified seconds
    time.sleep(run_delay)
    num += 1

# Save all the data that was collected and stored in the data array to a file
np.savetxt(file_name, 
           data,
           delimiter=",",
           fmt='%1.3f')

print(Back.GREEN +
      'Saved data to ' + file_name +
      Style.RESET_ALL)
