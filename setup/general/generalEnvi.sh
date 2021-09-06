#!/sh

# run this script using source

echo installing python packages:
# Updating pip
python3 -m pip install --upgrade pip

# install packages from requirements file
pip install -r requirements.txt

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

