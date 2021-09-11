# Python Setup

These instructions will walk you through installing python and creating a virtual environment to use as a workspace for project related tasks.
 
1. Within the terminal, install python 3 and related packages using the command  
    `$ sudo apt install python3-pip python3-dev`
2. Make sure to have every package on your system up-to-date so there aren't any dependency issues:  
    `$ sudo apt update`  
    `$ sudo apt upgrade`
3. Upgrade pip by running:  
    `$ python3 -m pip install --upgrade pip`
4. Install the ability to construct a virtual environment by running:  
    `$ sudo -H pip3 install virtualenv`
5. Create a directory on your computer related to all project tasks (e.g., `Workspace/`). This directory will store your base virtual environment, SageEdu Github repo, future virtual environments and GitHub repositories. 
6. Use the command `$ virtualenv ./base_env` within `Workspace/`, where `base_env` is the name of the virtual environment. **Keep that virtual environment name, and this will be known as the base environment**
	1. **Important:** Do not ever edit this folder
7. Activate the environment with the command:  
    `$ source base_env/bin/activate`
	1. Your command prompt should read something similar to:  
	    `(base_env)user@host:~/Workspace$`
	2. **Note:** Always activate your virtual environment whenever you start working with the packages you install within it and for work related tasks. And deactivate it with `(base_env)user@host:~$ deactivate` when you are done working.
	3. With this virtual environment, site packages and dependencies can be organized separate from the rest of the machine, so always be conscious of where you are working
8. Run the command:  
    `(base_env)user@host:~$ python3 -m pip install --upgrade pip`
9. We will now add an important command to the startup files of the terminal so that packages install and run correctly in the virtual environment. **Only necessary once per nano machine**
	1. Deactivate your virtual environment and run the command  
	    `$ vi ~/.bashrc` 
	2. Click the letter "i" on your keyboard to go into insert mode (able to edit the file)
	3. Use your arrow keys to go to the bottom of the file
	4. Add the command `export OPENBLAS_CORETYPE=ARMV8` at the very bottom, and you can choose to add a comment on top of it saying "# resolves illegal construction error and package installation errors"
	5. Click the "escape" key on your keyboard, type ":wq", and hit "enter" or "return" on your keyboard
	6. Exit out of all terminal windows because the change only takes place in new terminal windows 

You now have a working virtual environment to use throughout the `camera, microphone, and enviSensor` directories! And you can create countless more following steps 2 & 5-8!

**Important:** Never install packages using `sudo ...` commands within the virtual environment because it will cause dependency issues, so instead, install packages with `pip install ...` or any other way that does not run root permissions within the virtual environment (e.g., `python3 -m pip install ...`). If it's necessary to install something to root, do so outside of the virtual environment (e.g., installing tshark, libportaudio2). Though, this may require you to run the program outside of the virtual environment. If in doubt, look up what each part of a command does. Everything that can be done by a system setup can be done within a virtual environment. Just make sure to install the appropriate packages correctly.

**Next read the [GitHub setup instructions](https://github.com/ddiLab/SageEdu/blob/main/setup/general/githubSetup.md).**
