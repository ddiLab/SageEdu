<h1>Enviornmental Sensor</h1>

This directory contains instructions on how to set up the BME680 enviornmental sensor with your Jetson Nano, along with some example code.  
See the <a href='https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-bme680-breakout'>official BME680 breakout documentation</a> 
for even more information on the sensor.

---

<h2>Reference:</h2>

<h3>Sensor Setup:</h3>

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

<h3>Checking if Sensor is Ready:</h3>

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


<h2>Directory Contents:</h2>

<h2>setup.md</h2>

* This contains instructions on how to setup the enviornmental sensor with the Nano

<h2>enviSensorDemo.ipynb</h2>

* A jupyter notebook demonstrating and explaining how to take readings from the sensor

<h2>collectDataHour.py</h2>

* A python script that takes readings of humidity, air pressure, temperature, and gas resistance every minute for an hour and saves it to a csv file

<h2>hourData.csv</h2>

* Pre-recorded data from the sensor. Measurments of each type were taken once every minute over the course of an hour. The data has not been cleaned up and my contain outlying values.

<h2>images/</h2>

* A directory containing images used throught the documetation of the enviornmental sensor

<h2>readme.md</h2>

* This file
