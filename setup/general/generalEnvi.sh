#!/bin/sh

# Updating pip
python3 -m pip install --upgrade pip

# Jupyter Notebook
pip install notebook

# Required for creating plots
pip install matplotlib

# Libaries required for camera
pip install opencv-python
pip install Pillow

# Libaries required for enviornmental sensor
pip install bme680
pip install numpy

# Required for microphone
pip install scipy
pip install sounddevice

# Install Linux Packages
## exit out of environment
deactivate

## camera setup
sudo apt-get install network-manager -y
sudo apt-get install tshark -y

## microphone setup
sudo apt-get install libportaudio2 -y
