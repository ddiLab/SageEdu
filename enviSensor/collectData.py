"""
This script takes readings of humidity, air pressure, temperature,
and gas resistance every minute for an hour and saves it to a csv file.
"""

# Set up
import bme680
import time
import numpy as np
import sys

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
run_time = int(sys.argv[1])

# Number of minutes data has been collected
live_time = 0

# A 2D array where the collected data will be stored
data = [[0,0,0,0,0]]

# Gets initial readings from sensor to "start it up"
if sensor.get_sensor_data():
    sensor.data.temperature
    sensor.data.pressure
    sensor.data.humidity
    if sensor.data.heat_stable:
        sensor.data.gas_resistance

print('Collecting data for ' + str(run_time) + ' mins')
        
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
        
        # The array with the last set of readings is added to
        # the 2D array containing all the data
        data = np.append(data, reading, axis=0)
        
    else:
        # No data is available
        np.append(data, [[live_time,0,0,0,0]], axis=0)
    
    # Increments the number of minutes data has been collected
    live_time += 1
    
    # Waits 60 seconds before going back to the beginning of the loop
    # and taking the next measurement
    time.sleep(60)

# Save all the data that was collected and stored in the data array
# to a hourData.csv file
np.savetxt(str(sys.argv[2]), 
           data,
           delimiter=",",
           fmt='%1.3f')