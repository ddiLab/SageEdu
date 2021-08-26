# Virtual enviornment setup
virtualenv ./enviEnvi
source enviEnvi/bin/activate

# Updating pip
python3 -m pip install --upgrade pip

# Installing required libaries
python3 -m pip install --upgrade notebook
python3 -m pip install --upgrade bme680
python3 -m pip install --upgrade numpy
python3 -m pip install --upgrade matplotlib