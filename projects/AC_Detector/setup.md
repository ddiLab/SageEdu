# Instructions on setting up for project 1 -- an AC Detector
These instructions include the creation of a virtual environment solely for this project and installation of an audio analysis library   

Before you proceed, it's important to mention installation of pyAudioAnalysis could take upwards of two hours

## automated process
The following will take you through executing a script that will set up everything necessary for this project: 
1. run the script `setup_script.sh` from **within** the base environment created in the `SageEdu/setup/general` instructions and **inside** the current directory (`SageEdu/projects/AC_Detector`)
 1. it will automatically execute all the steps in the two sections below, creating a virtual environment, installing pyAudioAnalysis, extra packages, and cloning the repo of pyAudioAnalysis to the parent directory that houses your base virtual environment, pywaggle, and SageEdu directories.
 2. command: `source setup_script.sh`
 3. The script will require you to enter your password at some point

And of course, feel free to take a look at what the script does! There are some commented lines for clarity and an alternative way to install pyAudioAnalysis.

## creating virtual environment
1. Make sure the system is up-to-date
2. Install every python package from the base environment to the project 1 environment that will be created
 1. copy those packages with `pip freeze > reqs.txt`
 2. create the project 1 virtual environment with `virtualenv AC_Detector_env`
 3. activate it and upgrade pip with `source project1/bin/activate` and `python3 -m pip install --upgrade pip`
 4. install the stored required python packages with `pip install -r reqs.txt`
 5. delete that file because it is no longer needed with `rm reqs.txt`
 6. These steps will create a virtual environment folder in the directory that includes the base environment folder, pywaggle, and pyAudioAnalaysis

## install pyAudioAnalysis
1. Deactivate the virtual environment
2. Run the command `sudo apt-get install gcc gfortran python3-dev libopenblas-dev liblapack-dev libfreetype6-dev python3-tk`
3. Clone the pyAudioAnalysis repo to the parent directory of SageEdu, pywaggle, base environment directories with `git clone https://github.com/tyiannak/pyAudioAnalysis.git`
4. Reactivate the virtual environment (if using one)
5. Enter the pyAudioAnalysis repo
6. Run the command `pip install -r requirements.txt`
7. Run the command `pip install -e .`
8. Note: installing pyAudioAnalysis is now available in any virtual environment with the root changes implemented above
9. Refer to the library's [GitHub Repo](https://github.com/tyiannak/pyAudioAnalysis) for more information


**Next look at the [pyAudioAnalysis tutorial](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/pyAudioAnalysisIntroduction.ipynb)**
