# Instructions on setting up environment for an AC Detector
These instructions include the creation of a virtual environment solely for this project and installation of an audio analysis library.   

Before you proceed, it's important to mention installation of pyAudioAnalysis could take upwards of two hours

## automated process
The following will take you through executing a script that will set up everything necessary for this project: 
1. run the script `setup_script.sh` from **within** the base environment created in the `SageEdu/setup/general` instructions and **inside** the current directory (`SageEdu/projects/AC_Detector`)
 1. it will automatically execute all the steps in the two sections below: creating a virtual environment, installing pyAudioAnalysis, extra packages, and cloning the repo of pyAudioAnalysis to the parent directory that houses your base virtual environment, pywaggle, and SageEdu directories.
 2. command: `source setup_script.sh`
 3. the script will require you to enter your password at some point

And of course, feel free to take a look at what the script does! There are some commented lines for clarity and an alternative way to install pyAudioAnalysis.

## creating virtual environment
1. Make sure the system is up-to-date
2. Install every python package from the base environment to the project 1 environment that will be created
 1. copy those packages with `pip freeze > reqs.txt`
 2. create the project 1 virtual environment with `virtualenv AC_Detector_env`
 3. activate it with `source project1/bin/activate` 
 4. install specific versions of pip, setuptools, and wheel with `pip install pip==21.2.4 setuptools==57.4.0 wheel==0.36.2`
 5. install the stored required python packages with `pip install -r reqs.txt`
 6. delete that file because it is no longer needed with `rm reqs.txt`
 7. These steps will create a virtual environment folder in the directory that includes the base environment folder, pywaggle, and pyAudioAnalaysis

## install pyAudioAnalysis
1. Deactivate the virtual environment
2. Run the command `sudo apt-get install gcc gfortran python3-dev libopenblas-dev liblapack-dev libfreetype6-dev python3-tk`
3. Clone the pyAudioAnalysis repo to the parent directory of SageEdu, pywaggle, base environment directories with `git clone https://github.com/tyiannak/pyAudioAnalysis.git`
4. Reactivate the virtual environment (if using one)
5. Enter the pyAudioAnalysis repo
6. Reset the repo to a specific version using `git reset --hard 03c3fb5f8a7d2c4db2ae9c3155e7741faeab12e1`
7. Run the command `pip install -r requirements.txt`
8. Run the command `pip install -e .`
9. Note: installing pyAudioAnalysis is now available in any virtual environment with the root changes implemented above
10. Refer to the library's [GitHub Repo](https://github.com/tyiannak/pyAudioAnalysis) for more information, or the website of the [specific version installed](https://github.com/tyiannak/pyAudioAnalysis/tree/03c3fb5f8a7d2c4db2ae9c3155e7741faeab12e1)


**Next look at the [pyAudioAnalysis tutorial](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/pyAudioAnalysisIntroduction.ipynb)**
