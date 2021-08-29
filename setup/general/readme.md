# General Setup
This directory includes various files with instructions on further setting up the nano, regardless of initial headful or headless setup.  
Please go through these files for a stable working environment on the nano.  

Follow them in this order:

1. [pythonSetup](https://github.com/ddiLab/SageEdu/blob/main/setup/general/pythonSetup.md)
2. [githubSetup](https://github.com/ddiLab/SageEdu/blob/main/setup/general/githubSetup.md)
3. [PackageInstallationGuide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/PackageInstallationGuide.md)  
  
After completing the above steps, you are all done with the setup directory! Head back to the [main page](https://github.com/ddiLab/SageEdu).

---

## Directory Contents

### [linux_packages.sh](https://github.com/ddiLab/SageEdu/blob/main/setup/general/linux_packages.sh)
* Shell program that installs linux packages
* Before proceeding, refer to `PackageInstallationGuide.md` first

### [requirements.txt](https://github.com/ddiLab/SageEdu/blob/main/setup/general/requirements.txt)
* Text file that contains the necessary python packages for this repository
* Before proceeding, refer to `PackageInstallationGuide.md` first

### [stable_requirements.txt](https://github.com/ddiLab/SageEdu/blob/main/setup/general/stable_requirements.txt)
* Text file that contains a list of python pacakges and their versions for installation
* These specific pacakges have been extensively tested in the creation of this repository and should serve as a fail-safe for dependency issues
* Before proceeding, refer to `PackageInstallationGuide.md` first

### [AudioLibrariesSetup.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/AudioLibrariesSetup.md)
* Contains instructions on how to install the pyAudioAnalysis and Librosa python audio analysis libraries
* Before proceeding, refer to `PackageInstallationGuide.md` first

### [JupyterNotebookSetup.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/JupterNotebookSetup.md)
* Contains instructions on how to set up Jupyter Notebook
* Before proceeding, refer to `PackageInstallationGuide.md` first

### [jupyterNotebookTutorial.ipynb](https://github.com/ddiLab/SageEdu/blob/main/setup/general/jupyterNotebookTutorial.ipynb)
* A Jupyter Notebook with instructions on how to use Jupyter Notebooks

### [PackageInstallationGuide.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/PackageInstallationGuide.md)
* Contains instructions on how to properly install linux and python packages
* **A must read**

### [pythonSetup.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/pythonSetup.md)
* Contains the necessary steps to install python and create a virtual environment
* To reiterate, everything can be done with a virtual environment as working without one, but always make sure to install packages with `pip install ...`and not `sudo ...` within the virtual environment. 

### [githubSetup.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/githubSetup.md)
* Includes instructions on how to create a local repository from Github
* Some useful git commands to use:
    * `$ git add` adds changes from a file/directory (including new files) to commit, essentially staging a commit
    * `$ git commit -m "[Commit Message]"` commits the changes of a file/directory, preparing them to be sent to Github
    * `$ git push` pushes all the commits to the repository on Github. Make sure it went through by checking Github for changes
    * `$ git pull` updates your local repo with the one on Github
    * `$ git status` lists all the changes of your local repo from that on Github, including which ones are added committed, or neither
* Note: always make sure to pull any changes from Github before editing your local repo and pushing

### [readme.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/readme.md)
* This file
