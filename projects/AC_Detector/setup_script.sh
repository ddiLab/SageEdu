#!/bachrc
# run in VE from set up instructions

echo Creating virtual environment for AC detector project
# set up base VE
pip freeze > reqs.txt
virtualenv AC_Det
source AC_Det/bin/activate
python3 -m pip install --upgrade pip
pip install -r reqs.txt
rm reqs.txt

## install linux packages
deactivate
sudo apt-get install gcc gfortran python3-dev libopenblas-dev liblapack-dev libfreetype6-dev python3-tk -y
source AC_Det/bin/activate

## install pyAudioAnalysis
git clone https://github.com/tyiannak/pyAudioAnalysis.git
cd pyAudioAnalysis/
pip install -r requirements.txt
pip install -e .
cd ..
# option to remove it sudo rm -rf pyAudioAnalysis

## confirmation
echo Install successful!

