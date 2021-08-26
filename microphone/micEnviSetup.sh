# Virtual enviornment setup
virtualenv ./micEnvi
source micEnvi/bin/activate

# Updating pip
python3 -m pip install --upgrade pip

# Installing required libaries
python3 -m pip install --upgrade notebook
python3 -m pip install --upgrade scipy
python3 -m pip install --upgrade matplotlib