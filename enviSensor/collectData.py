"""
This script takes readings of humidity, air pressure, temperature,
and gas resistance every minute and saves it to a file.
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

# Number of minutes to collect data
run_time = int(sys.argv[2])

# Number of minutes data has been collected
live_time = 0

# A 2D array where the collected data will be stored
data = [[0,0,0,0,0]]

# Sensor burn in
print(Back.GREEN +
      'Burnning in for ' + str(sys.argv[1]) + ' mins' +
      Style.RESET_ALL)
for x in range (0, int(sys.argv[1]) * 60):
    if sensor.get_sensor_data():
        sensor.data.temperature
        sensor.data.pressure
        sensor.data.humidity

        if sensor.data.heat_stable:
            sensor.data.gas_resistance

        time.sleep(1)
        
print(Back.GREEN +
      'Collecting data for ' + str(run_time) + ' mins' +
      Style.RESET_ALL)
     
while live_time < run_time + 1: 
    if sensor.get_sensor_data():
        if sensor.data.heat_stable:
            # Takes a reading of everything and stores it in an array
            reading = [[live_time,
                        sensor.data.temperature,
                        sensor.data.pressure,
                        sensor.data.humidity,
                        sensor.data.gas_resistance]]
        else:
            # Gas resistance reading cannot be taken
            reading = [[live_time,
                        sensor.data.temperature,
                        sensor.data.pressure,
                        sensor.data.humidity,
                        -1]]
            print(Fore.YELLOW +
                  'Warning: Gas resistance data could not be collected at minute ' +
                  str(live_time) +
                  Style.RESET_ALL)
        
        # The array with the last set of readings is added to
        # the 2D array containing all the data
        data = np.append(data, reading, axis=0)
        
        print('Data collected at minute ' + str(live_time) + ' of ' + str(run_time)) 
        
    else:
        # No data is available
        np.append(data, [[live_time,-1,-1,-1,-1]], axis=0)
        print(Fore.YELLOW +
              'Warning: No data could be collected at minute ' +
              str(live_time) +
              Style.RESET_ALL)
    
    # Increments the number of minutes data has been collected
    live_time += 1
    
    if live_time < run_time + 1:
        # Waits 60 seconds before going back to the beginning of the loop
        # and taking the next measurement
        time.sleep(60)

# Removes the firt row of 0s in the data array
data = np.delete(data, (0), axis=0)
    
# Save all the data that was collected and stored in the data array to a file
np.savetxt(str(sys.argv[3]), 
           data,
           delimiter=",",
           fmt='%1.3f')

print(Back.GREEN +
      'Saved data to ' + str(sys.argv[3]) +
      Style.RESET_ALL)