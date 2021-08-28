# ! Run this from within the SageEdu/setup/general directory !

# Virtual enviornment setup
virtualenv ../../generalEnvi
source ../../generalEnvi/bin/activate

# Updating pip
python3 -m pip install --upgrade pip

# Jupyter Notebook
python3 -m pip install --upgrade notebook

# Required for creating plots
python3 -m pip install --upgrade matplotlib

# Libaries required for camera
python3 -m pip install --upgrade opencv-python
python3 -m pip install --upgrade Pillow

# Libaries required for enviornmental sensor
python3 -m pip install --upgrade bme680
python3 -m pip install --upgrade numpy

# Required for microphone
python3 -m pip install --upgrade scipy
