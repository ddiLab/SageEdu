# Instructions on setting up for project 1 -- an AC Detector
These instructions include the creation of a virtual environment solely for this project and installation of an audio analysis library   

Before you proceed, it's important to mention:
1. Installation of pyAudioAnalysis could take upwards of two hours
2. **can be archived** The librosa library will require packages not included in its installation (e.g., numpy, audioread, scikit-learn). So to ensure a smooth installation, install pyAudioAnalysis first. Or you can take a look at the [setup requirements](https://github.com/librosa/librosa/blob/90cef6fb5a38261eb2076d3e00aad4927400353f/setup.cfg) and install them individually

## automated process
* Note: run the script `setup_script.sh` from **within** the base environment created in the `setup` instructions to automatically execute all the steps below for the creation of the virtual environment and pyAudioAnalysis install
 * command: `bash setup_script.sh`
 * this script will create a new virtual environment specifically for this project. It will include extra packages and will also clone an audio analysis library

## creating virtual environment
1. Make sure the system is up-to-date
2. Install every python package from the base environment to the project 1 environment that will be created
 1. copy those packages with `pip freeze > reqs.txt`
 2. create the project 1 virtual environment with `virtualenv project1`
 3. activate it and upgrade pip with `source project1/bin/activate` and `python3 -m pip install --upgrade pip`
 4. install the stored required python packages with `pip install -r reqs.txt`
 5. delete that file because it is no longer needed with `rm reqs.txt`

## install pyAudioAnalysis
1. Deactivate the virtual environment
2. Run the command `sudo apt-get install gcc gfortran python3-dev libopenblas-dev liblapack-dev libfreetype6-dev python3-tk`
3. Clone the pyAudioAnalysis repo with `git clone https://github.com/tyiannak/pyAudioAnalysis.git`
4. Reactivate the virtual environment (if using one)
5. Enter the repo with `cd pyAudioAnalysis/`
6. Run the command `pip install -r requirements.txt`
7. Run the command `pip install -e .`
8. Note: installing pyAudioAnalysis is now available in any virtual environment with the root changes implemented above
9. Refer to the library's [GitHub Repo](https://github.com/tyiannak/pyAudioAnalysis) for more information

## Librosa **can be archived**
1. Make sure the system is up-to-date and you have the required packages installed
2. Outside of the virtual environment (if using one), run `sudo apt-get install llvm-10*`
3. Run `sudo -i`
4. Run `cd /usr/bin/`
5. Run `rm llvm-config` (if the file exists)
6. Run `ln -s llvm-config-10 llvm-config`
    1. This will redirect the llvm-config file to llvm-10, which is necessary to install llvmlite (a dependency for the librosa library)
7. Refresh the terminal and go back to where the library and accompanying packages should be installed
8. Run `pip install librosa`
9. Note: installing librosa is now available in any virtual environment with the root changes implemented above
10. Refer to the library's [website](https://librosa.org) for more information
