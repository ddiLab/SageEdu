# Environmental Sensor Sample Programs

This directory contains basic programs that make use of the environmental sensor.

---

## Directory Contents:

### [Data Plots.ipynb](https://github.com/ddiLab/SageEdu/blob/dev/enviSensor/sample_programs/Data%20Plots.ipynb)
* Notebook containing plots of various datasets collected using the sensor

### [changeAlert.ipynb](https://github.com/ddiLab/SageEdu/blob/dev/enviSensor/sample_programs/changeAlert.ipynb)
* A jupyter notebook containing code that calculates the normal state of the enviornment, then alerts you if there are abnormal changes in the enviornment

### [burnInPlots.ipynb](https://github.com/ddiLab/SageEdu/blob/dev/enviSensor/sample_programs/burnInPlots.ipynb)
* A jupyter notebook containing plots of the datasets collected from various burn-in tests

### [collectData.py](https://github.com/ddiLab/SageEdu/blob/dev/enviSensor/sample_programs/collectData.py)
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

### [burnInTests/](https://github.com/ddiLab/SageEdu/tree/dev/enviSensor/sample_programs/burnInTests)
* A directory containing data from various burn in tests

### [readme.md](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/readme.md)
* This file
