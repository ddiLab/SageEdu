#!/sh
# run with source

echo Creating virtual environment for AC detector project
# set up base VE
pip freeze > reqs.txt
deactivate
virtualenv ../../../AC_Detector_env
source ../../../AC_Detector_env/bin/activate
pip install pip==21.2.4 setuptools==57.4.0 wheel==0.37.0
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
cd ../../../pyAudioAnalysis
git reset --hard 03c3fb5f8a7d2c4db2ae9c3155e7741faeab12e1
pip install -r requirements.txt
echo feel free to ignore the possible error above because it only causes problems when using python 3.7+ with the tensorflow library in image analysis. Install opencv-python==4.4.0.46 if errors do occur
pip install -e .
cd ../SageEdu/projects/AC_Detector

## confirmation
echo Install successful!

