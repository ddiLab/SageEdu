# General Setup
This directory includes various files with instructions on further setting up the nano, regardless of initial headful or headless setup.  
Please go through these files for a stable working environment on the nano.  

Follow them in this order:

1. [pythonSetup](https://github.com/ddiLab/SageEdu/blob/main/setup/general/pythonSetup.md)
2. [githubSetup](https://github.com/ddiLab/SageEdu/blob/main/setup/general/githubSetup.md)
3. [PackageInstallationGuide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/PackageInstallationGuide.md)
4. [JupyterNotebookSetup](https://github.com/ddiLab/SageEdu/blob/main/setup/general/JupyterNotebookSetup.md)
5. [jupyterNotebookTutorial](https://github.com/ddiLab/SageEdu/blob/main/setup/general/jupyterNotebookTutorial.ipynb)
  
After completing the above steps, you are all done with the setup directory! Head back to the [main page](https://github.com/ddiLab/SageEdu).

---

## Directory Contents

### [requirements.txt](https://github.com/ddiLab/SageEdu/blob/main/setup/general/requirements.txt)
* List of python packages installed by `generalEnvi.sh` with specific versions

### [generalEnvi.sh](https://github.com/ddiLab/SageEdu/blob/main/setup/general/generalEnvi.sh)
* Shell program that further customizes the base environment (`base_env`) to make it workable with the `camera, microphone, enviSensor` directories

### [JupyterNotebookSetup.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/JupyterNotebookSetup.md)
* Contains instructions on how to set up Jupyter Notebook

### [jupyterNotebookTutorial.ipynb](https://github.com/ddiLab/SageEdu/blob/main/setup/general/jupyterNotebookTutorial.ipynb)
* A Jupyter Notebook with instructions on how to use Jupyter Notebooks

### [PackageInstallationGuide.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/PackageInstallationGuide.md)
* Contains instructions on how to properly install linux and python packages for the current repository

### [pythonSetup.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/pythonSetup.md)
* Contains the necessary steps to install python and create the base virtual environment
* To reiterate, everything can be done with a virtual environment as working without one, but always make sure to install packages with `pip install ...`and not `sudo ...` within the virtual environment. 

### [githubSetup.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/githubSetup.md)
* Includes instructions on how to create a local repository from Github by cloning the current repo
* Some useful git commands to use:
    * `$ git add` adds changes from a file/directory (including new files) to commit, essentially staging a commit
    * `$ git commit -m "[Commit Message]"` commits the changes of a file/directory, preparing them to be sent to Github
    * `$ git push` pushes all the commits to the repository on Github. Make sure it went through by checking Github for changes
    * `$ git pull` updates your local repo with the one on Github
    * `$ git status` lists all the changes of your local repo from that on Github, including which ones are added committed, or neither
* Note: always make sure to pull any changes from Github before editing your local repo and pushing

### [readme.md](https://github.com/ddiLab/SageEdu/blob/main/setup/general/readme.md)
* This file
