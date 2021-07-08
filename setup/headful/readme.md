<h1>Headful Mode Setup</h1>

This directory contains instructions on how to set up the Jetson Nano in headful mode.

Headful mode requires the use of a monitor, keyboard, mouse, and another computer. 
Setting up the Nano headful allows it to be used via a GUI.

<h2>setup.md</h2>

* Contains instructions on how to perform the basic initial setup of the Nano

<h2>virtualEnvironmentSetup.md</h2> 

* Note: optional method for setting up python work space 
* Contains the necessary steps to create a virtual environment and instructions on how to install packages
* To reiterate, everything can be done with a virtual environment as working without one, but always make sure to install packages with `pip install ...`and not `sudo ...` within the virtual environment. 

<h2>jupyterNotebookSetup.md</h2> 

* Contains instructions on how to set up Jupyter Notebook

<h2>githubSetup.md</h2> 

* Includes instructions on how to create a local repository from Github
* Some useful git commands to use:
    * `$ git add` adds changes from a file/directory (including new files) to commit, essentially staging a commit
    * `$ git commit -m "[Commit Message]"` commits the changes of a file/directory, preparing them to be sent to Github
    * `$ git push` pushes all the commits to the repository on Github. Make sure it went through by checking Github for changes
    * `$ git pull` updates your local repo with the one on Github
    * `$ git status` lists all the changes of your local repo from that on Github, including which ones are added committed, or neither
* Note: always make sure to pull any changes from Github before editing your local repo and pushing

<h2>/images</h2> 

* A directory containing images referenced in the instructions

<h2>readme.md</h2>

* This file
