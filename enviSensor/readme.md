# Enviornmental Sensor

This directory contains instructions on how to set up the BME680 enviornmental sensor with your Jetson Nano, along with some example code.  
See the <a href='https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-bme680-breakout'>official BME680 breakout documentation</a> 
for even more information on the sensor.

---

## Reference

### Sensor Setup

```
sensor = bme680.BME680()

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)
```

### Checking if Sensor is Ready

General Sensor Check:
`sensor.get_sensor_data()`

Hot Plate Check:
`sensor.data.heat_stable`

<h3>Reading from Sensor</h3>

Temperature:
`sensor.data.temperature`

Air Pressure:
 `sensor.data.pressure`
 
Humidity:
 `sensor.data.humidity`
 
Gas Resistance:
 `sensor.data.gas_resistance`
 
 ---

## Directory Contents

### [setup.md](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/setup.md)
* This contains instructions on how to setup the enviornmental sensor with the Nano

### [enviSensorDemo.ipynb](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/enviSensorDemo.ipynb)
* A jupyter notebook demonstrating and explaining how to take readings from the sensor

### [changeAlert.ipynb](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/changeAlert.ipynb)
* A jupyter notebook containing code that calculates the normal state of the enviornment, then alerts you if there are abnormal changes in the enviornment

### [burnInPlots.ipynb](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/burnInPlots.ipynb)
* A jupyter notebook containing plots of the datasets collected from various burn-in tests

### [dataPlots.ipynb](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/Data%20Plots.ipynb)
* A jupyter notebook containing plots of various datasets collected from the sensor

### [collectData.py](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/collectData.py)
* A python script that takes readings of humidity, air pressure, temperature, and gas resistance every minute for given amount of minutes and saves it to a csv file
* Run the scrip by running the following command:  
  `python3 collectData.py BURN_IN_DELAY BURN_IN_TIME RUN_DELAY RUN_TIME FILE_NAME`    
  * `BURN_IN_DELAY` is the number of seconds between readings during the burn-in process
  * `BURN_IN_TIME` is the number of minutes you want the sensor to burn in
  * `RUN_DELAY` is the number of seconds between measurments
  * `RUN_TIME` is the number of minutes you want the script to run
  * `FILE_NAME` is the name of the file you want the date to be stored in. This should end in ".csv"
* For example, run the following command to burn in for 20 minutes then collect data for an hour and save it to a file called `hour_data.csv`:  
    `python3 collectData.py 2 20 60 60 'hour_data.csv'`

### [hourData.csv](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/hourData.csv)
* Pre-recorded data from the sensor. Measurments of each type were taken once every minute over the course of an hour. The data has not been cleaned up and my contain outlying values.

### [burnInTests/](https://github.com/ddiLab/SageEdu/tree/main/enviSensor/burnInTests)
* A directory containing data from various burn in tests

### [images/](https://github.com/ddiLab/SageEdu/tree/main/enviSensor/images)
* A directory containing images used throught the documetation of the enviornmental sensor

### [readme.md](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/readme.md)
* This file
