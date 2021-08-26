<h1>Enviornmental Sensor Setup</h1>

1. Connect in the 5 pin USB cable into the environmental sensor with the black wire connected to the ground pin
  <img alt='Envi Sensor Image' src='./images/envi.jpeg'></img>

2. With the Nano powered off, connect the other end of the cable into the nano on the bottom leftmost set of 5 pins on the 40-pin expansion header.
The black wire should connect to the ground pin and the red wire should connect to the pin labeled 3v3
  <img alt='Pins on Board Image' src='./images/envi-board.jpeg'></img>

3. Turn on the Nano

## Python Enviornment
1. To create a virtual enviornment with all the packages you need to work through the tutorials simply run the folloing command from within the `enviSensor/` directory:  
    `bash enviSensorEnviSetup.sh`
    * If you want to set everything up on your own, open up the `enviSensor/enviSensorEnviSetup.sh` file and take a look at what its doing. If something in that file seems confusing, take a look at either the [Python Setup Guide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/pythonSetup.md) or the [Package Installation Guide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/PackageInstallationGuide.md).

2. Activate the virtual enviornment by running:  
    `source enviEnvi/bin/activate`

3. Start a jupyter notebook server by running:  
    `jupyter notebook`

4. See `enviSensor/enviSensorDemo.ipynb` for more information on the sensor including how to interact with it using Python.
