# Enviornmental Sensor

This directory contains instructions on how to set up the BME680 enviornmental sensor with your Jetson Nano, along with some example code.  

Start with [setup.md](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/setup.md). And then 
1. [enviSensorDemo.ipynb](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/enviSensorDemo.ipynb)
2. [sample_programs/](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/sample_programs)

Or feel free to explore the directory on your own!

See the <a href='https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-bme680-breakout'>official BME680 breakout documentation</a> 
for even more information on the sensor.

---

## Reference

### Sensor Setup
Code snippet used to set up the sensor for any python program:

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

### Reading from Sensor

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
* Contains instructions on how to setup the enviornmental sensor with the Nano

### [hour_data.csv](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/hour_data.csv)
* Pre-recorded data from the sensor used in the `enviSensorDemo.ipynb` notebook
* Measurments of each type were taken once every 10 seconds over the course of an hour

### [enviSensorDemo.ipynb](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/enviSensorDemo.ipynb)
* A jupyter notebook demonstrating and explaining how to take readings from the sensor

### [sample_programs/](https://github.com/ddiLab/SageEdu/tree/main/enviSensor/sample_programs)
* A directory containing extra python scripts and notebooks on interpreting sensor data and collecting it

### [images/](https://github.com/ddiLab/SageEdu/tree/main/enviSensor/images)
* A directory containing images used in the `setup.md` file

### [readme.md](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/readme.md)
* This file
