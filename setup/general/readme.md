<h1>General Setup</h1>
This directory includes various files with instructions on further setting up the nano, regardless of initial headful or headless setup.  
Please go through these files for a stable working environment on the nano

---

<h2>linux_packages.sh</h2> 

* Shell program that installs linux packages
* Before proceeding, refer to `PackageInstallationGuide.md` first

<h2>requirements.txt</h2> 

* Text file that contains the necessary python packages for this repository
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