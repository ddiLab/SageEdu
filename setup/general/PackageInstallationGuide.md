# Package Installation Guide
This file will guide you through how to install various packages and libraries. Before proceeding, it's important that your linux environment is fully functional by completing all the steps in either the headful or headless directory.

## Linux packages
These are packages that are used system wide. It's a good habit to keep all pacakges up-to-date before installing any new ones. If anywhere throughout this repository a package needs to be installed, it will be clearly indicated with accompanying instructions. 

**Note:** Linux packages should be installed outside a virtual environment.

### General Commands
* **Installing:** `sudo apt-get install <package>`
* **Removing:**
    * `sudo apt-get remove <package>` to remove a package
    * `sudo apt-get --purge remove <package>` to remove a package AND its configuration files
* **Updating:** `sudo apt-get update` to download updates
* **Upgrading:** `sudo apt-get upgrade` to install updates
* **Listing:**
    * `sudo apt list --upgradable` to view the packages that can be upgraded
    * `dpkg --list` to view all system packages


## Python packages
These are packages installed by pip (package-management-system) for python usage
1. Make sure pip is updated with the command `python3 -m pip install --upgrade pip`
2. `python3 -m pip ...` is the same as `pip3 ...`. And within a virtual environement, `pip3` isn't even necessary; you can just use `pip ...`. But make sure to use the appropriate handler, as installing with `pip` as opposed to `pip3` (not in a virtual environment) can cause problems. Going forward, I will just use `pip`

As always, make sure you install the python packages in the correct location. When using a virtual environment, install them inside it, but make sure to not execute any `sudo...` commands within it. If you're not using a virtual environment (not recommended), make sure to use `pip3` or `python3 -m pip` instead of `pip`.  
If anywhere throughout this repository a package needs to be installed, it will be clearly indicated with accompanying instructions.

### General Commands
* **Installing:** 
    * `pip install <package>` installs the most recent available version
    * `pip install <package>==<version>` installs a specific version
    * `pip install -r <file>` installs packages from a requirements file (usually labeled `requirements.txt`)
* **Removing:**
    * `pip uninstall <package>` to remove a package
* **Listing:**
    * `pip freeze` show every installed package in the environment and their versions

## Base Enviornment Customization
**Before proceeding, make sure to have completed the instructions in `/setup/general/pythonSetup.md`**   
To customize your current virtual enviornment with all the packages you need to follow the tutorials of the sensors, simply run the following command **within** your base environment **in** the current directory (`setup/general`):  
    `bash generalEnvi.sh`  

Note: that command will exit you of your virtual environment   

* If you want to set everything up on your own, open up the `/setup/general/generalEnvi.sh` file and take a look at what it's doing. If something in that file seems confusing, reread this document or take a look at the [Python Setup Guide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/pythonSetup.md).

    
**Next read the [Jupyter Notebook Setup Guide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/JupterNotebookSetup.md) to learn how to get started using jupyter notebooks!**
   
---
**Section below can be archived in the final version**
### Specific packages
As opposed to linux packages, it's advisable to install every package included in the `requirements.txt` file (found in the current directory) and the ones below because there are no other instructions in this repository on how to install them.
* **Important:** Since manging dependency issues with python packages is more troublesome than linux packages, `stable_requirements.txt` has also been included in this directory to eliminate this problem; it includes every extensively tested package and its version used throughout this repository. If there are installation errors or python errors with modules, **only** install pywaggle first, followed by `stable_requirements.txt` with`pip install -r stable_requirements.txt`. 

The following is the order in which specific libraries and packages should be installed:
1. Jupyter Notebook
2. `requirements.txt`
3. pywaggle
4. pyAudioAnalysis & Librosa  

* **Installing Jupyter Notebook:** follow the instructions in the `JupyterNotebookSetup.md` file
* **Installing `requirements.txt`:** run the command `pip install -r requirements.txt`
* **Installing pywaggle:** follow the installation guide on the [GitHub website](https://github.com/waggle-sensor/pywaggle)
* **Installing pyAudioAnalysis & Librosa:** follow the instructions in the `AudioLibrariesSetup.md` file

