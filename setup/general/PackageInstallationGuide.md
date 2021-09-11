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
2. `python3 -m pip ...` is the same as `pip3 ...`. And within a virtual environement, `pip3` isn't even necessary; you can just use `pip ...`. But make sure to use the appropriate handler, as installing with `pip` as opposed to `pip3` (outside a virtual environment) can cause problems. Going forward, I will just use `pip` since we'll be working with the base virtual environment.

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
To customize your current virtual enviornment with all the packages you need to follow the tutorials of the sensors, simply run the following command **within** your base environment **inside** the current directory (`setup/general`):  
    `source generalEnvi.sh`  

* The script will require your password at some point and will change the pip, setuptools, and wheel versions
* If you want to set everything up on your own, open the `/setup/general/generalEnvi.sh` file and take a look at what it's doing. If something in the file seems confusing, reread this document or take a look at the [Python Setup Guide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/pythonSetup.md).

    
**Next read the [Jupyter Notebook Setup Guide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/JupyterNotebookSetup.md) to learn how to get started using jupyter notebooks!**
