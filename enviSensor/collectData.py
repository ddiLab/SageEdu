"""
This script takes readings of humidity, air pressure, temperature,
and gas resistance and saves it to a file.
"""

# Required Libraries
import bme680
import time
import numpy as np
import sys
import colorama
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

        return reading
        
    else:
        # No data is available
        return 0


# Script Arguments
burn_delay = int(sys.argv[1]) # Time between each burn-in reading - (seconds)
burn_time  = int(sys.argv[2]) # Total burn-in time ---------------- (minutes)
run_delay  = int(sys.argv[3]) # Time between each measurment ------ (seconds)
run_time   = int(sys.argv[4]) # Total run time -------------------- (minutes)
file_name  = str(sys.argv[5]) # File name to save data


# Number of seconds data has been collected
live_time = 0

# A 2D array where the collected data will be stored
# First entry contains metadata
data = [[burn_delay, burn_time, run_delay, run_time, 0]]

# Sensor burn in
print(Back.GREEN +
      'Burnning in for ' + str(burn_time) + ' mins at ' +
      str(burn_delay) + ' sec intervals' +
      Style.RESET_ALL)

while live_time < burn_time * 60:
    get_all_readings()
    time.sleep(burn_delay)
    live_time += burn_delay

# Reset live_time to 0
live_time = 0
        
print(Back.GREEN +
      'Collecting data for ' + str(run_time) + ' mins at ' +
      str(run_delay) + ' sec intervals' +
      Style.RESET_ALL)
     
while live_time < (run_time + 1) * 60: 
    reading  = get_all_readings()
    if reading == 0:
        # No data is available
        np.append(data, [[live_time,-1,-1,-1,-1]], axis=0)
        print(Fore.YELLOW +
              'Warning: No data could be collected at ' +
              str(live_time) + ' seconds' +
              Style.RESET_ALL)

    else:
        if reading[3] == -1:
            print(Fore.YELLOW +
                    'Warning: Gas resistance data could not be collected at ' +
                    str(live_time) + ' seconds' +
                    Style.RESET_ALL)
            
        # The array with the last set of readings is added to
        # the 2D array containing all the data
        data = np.append(data, [[live_time,
                                 reading[0],
                                 reading[1],
                                 reading[2], 
                                 reading[3]]], axis=0)
            
        print('Data collected at ' + str(live_time) + ' seconds of ' +
        str(run_time) + ' minutes') 
        
    
    # Increments the number of minutes data has been collected
    live_time += run_delay
    
    if live_time < run_time + 1:
        # Waits 60 seconds before going back to the beginning of the loop
        # and taking the next measurement
        time.sleep(run_delay)
    
# Save all the data that was collected and stored in the data array to a file
np.savetxt(file_name, 
           data,
           delimiter=",",
           fmt='%1.3f')

print(Back.GREEN +
      'Saved data to ' + file_name +
      Style.RESET_ALL)