# Virtual enviornment setup
virtualenv ./camEnvi
source camEnvi/bin/activate

# Updating pip
python3 -m pip install --upgrade pip

# Installing required libaries
python3 -m pip install --upgrade notebook
python3 -m pip install --upgrade opencv-python
python3 -m pip install --upgrade Pillow