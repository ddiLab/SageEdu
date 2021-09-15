<h1>Enviornmental Sensor Setup</h1>

1. Connect in the 5 pin USB cable into the environmental sensor with the black wire connected to the ground pin
  <img alt='Envi Sensor Image' src='./images/envi.jpeg'></img>

2. With the Nano powered off, connect the other end of the cable into the nano on the bottom leftmost set of 5 pins on the 40-pin expansion header.
The black wire should connect to the ground pin and the red wire should connect to the pin labeled 3v3
  <img alt='Pins on Board Image' src='./images/envi-board.jpeg'></img>

3. Turn on the nano and clone the bme680 repository to the parent directory (e.g., Workspace) that houses this repo (SageEdu), pywaggle, and the base virtual environment.
    1. Once inside that parent directory, run the command `git clone https://github.com/pimoroni/bme680`

4. Enter the `examples/` folder of that directory and activate your base virtual environment

5. Run the program `read-all.py` to burn-in (configure and stabilize) the sensor
    1. command: `python3 read-all.py`
    2. per the results of [sample_programs/burnInPlots.ipynb](https://github.com/ddiLab/SageEdu/blob/main/enviSensor/sample_programs/burnInPlots.ipynb) and recommendations of the documenation below, keep the `read-all.py` script running for at least 20 minutes and let sensor rest for 5 minutes before taking measurements
    3. exit the program with `Ctrl + C` on keyboard

## Now the enviornmental sensor is all setup!

Optional: read the [BME680 breakout documentation](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-bme680-breakout) for extra information on interacting with the sensor.
