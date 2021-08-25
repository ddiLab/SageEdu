<h1>General Setup</h1>
This directory includes various files with instructions on further setting up the nano, regardless of initial headful or headless setup.  
Please go through these files for a stable working environment on the nano.  

Follow them in this order:

1. [pythonSetup](https://github.com/ddiLab/SageEdu/blob/main/setup/general/pythonSetup.md)
2. [githubSetup](https://github.com/ddiLab/SageEdu/blob/main/setup/general/githubSetup.md)
3. [PackageInstallationGuide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/PackageInstallationGuide.md)  
  
After completing the above steps, you are all done with the setup directory! Head back to the [main page](https://github.com/ddiLab/SageEdu).

---

<h2>linux_packages.sh</h2> 

* Shell program that installs linux packages
* Before proceeding, refer to `PackageInstallationGuide.md` first

<h2>requirements.txt</h2> 

* Text file that contains the necessary python packages for this repository
* Before proceeding, refer to `PackageInstallationGuide.md` first

<h2>stable_requirements.txt</h2> 

* Text file that contains a list of python pacakges and their versions for installation
* These specific pacakges have been extensively tested in the creation of this repository and should serve as a fail-safe for dependency issues
* Before proceeding, refer to `PackageInstallationGuide.md` first

<h2>AudioLibrariesSetup.md</h2> 

* Contains instructions on how to install the pyAudioAnalysis and Librosa python audio analysis libraries
* Before proceeding, refer to `PackageInstallationGuide.md` first

<h2>JupyterNotebookSetup.md</h2> 

* Contains instructions on how to set up Jupyter Notebook
* Before proceeding, refer to `PackageInstallationGuide.md` first

<h2>PackageInstallationGuide.md</h2> 

* Contains instructions on how to properly install linux and python packages
* **A must read**

<h2>pythonSetup.md</h2> 

* Contains the necessary steps to install python and create a virtual environment
* To reiterate, everything can be done with a virtual environment as working without one, but always make sure to install packages with `pip install ...`and not `sudo ...` within the virtual environment. 

<h2>githubSetup.md</h2> 

* Includes instructions on how to create a local repository from Github
* Some useful git commands to use:
    * `$ git add` adds changes from a file/directory (including new files) to commit, essentially staging a commit
    * `$ git commit -m "[Commit Message]"` commits the changes of a file/directory, preparing them to be sent to Github
    * `$ git push` pushes all the commits to the repository on Github. Make sure it went through by checking Github for changes
    * `$ git pull` updates your local repo with the one on Github
    * `$ git status` lists all the changes of your local repo from that on Github, including which ones are added committed, or neither
* Note: always make sure to pull any changes from Github before editing your local repo and pushing

<h2>readme.md</h2>

* This file
