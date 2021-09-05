#!/sh
# run with source

echo Creating virtual environment for AC detector project
# set up base VE
pip freeze > reqs.txt
deactivate
virtualenv ../../../AC_Detector_env
source ../../../AC_Detector_env/bin/activate
python3 -m pip install --upgrade pip
pip install -r reqs.txt
rm reqs.txt

## install linux packages
deactivate
echo installing linux packages
sudo apt-get install gcc gfortran python3-dev libopenblas-dev liblapack-dev libfreetype6-dev python3-tk -y
source ../../../AC_Detector_env/bin/activate

## install pyAudioAnalysis
echo installing pyAudioAnalysis
mkdir ../../../pyAudioAnalysis
git clone https://github.com/tyiannak/pyAudioAnalysis.git ../../../pyAudioAnalysis
pip install -r ../../../pyAudioAnalysis/requirements.txt
echo feel free to ignore the error above because it only causes problems when using python 3.7+ with the tensorflow library in image analysis
### install opencv-python==4.4.0.46 if errors do occur 

pip install -e ../../../pyAudioAnalysis/.
### installs specific version of pyAudio Analysis: pip install -e git+https://github.com/tyiannak/pyAudioAnalysis.git@944f1d777bc96717d2793f257c3b36b1acf1713a#egg=pyAudioAnalysispycparser==2.20

## confirmation
echo Install successful!

