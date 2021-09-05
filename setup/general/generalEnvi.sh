#!/sh

# run this script using source

echo installing python packages:
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

# install pywaggle
mkdir ../../../pywaggle
git clone https://github.com/waggle-sensor/pywaggle ../../../pywaggle
pip install ../../../pywaggle[dev]

echo success!

echo installing linux packages:
# Install Linux Packages

## exit environment
deactivate

## camera setup
sudo apt-get install network-manager -y
sudo apt-get install tshark -y

## microphone setup
sudo apt-get install libportaudio2 -y

## reactivate environment
source ../../../base_env/bin/activate

echo success!

