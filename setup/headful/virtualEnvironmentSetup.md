﻿## Creating a virtual environment to use as a workspace for Sage related tasks
1. Within the terminal, install python 3 and related packages using the command `$ sudo apt install python3-pip python3-dev`
2. Make sure to have every package on your system up-to-date by running the commands `$ sudo apt update` and `$ sudo apt upgrade`, so there aren't any dependency issues
3. Then run `$ python3 -m pip install --upgrade pip` to upgrade pip
4. Run the command `$ sudo apt install python3-venv` to install the ability to construct a virtual environment
5. Create a directory on your computer related to all Sage tasks (e.g., `/sageWorkspace`). This directory will store your virtual environment and Github repo (if you are using one)
6. Use the command `$ python3 -m venv /my_project_env` within `/sageWorkspace`, where `/my_project_env` is the name of the virtual environment you want to create, so make sure to name it appropriately 
	1. **Important:** Do not ever edit this folder
7. Activate the environment with the command `$ source my_project_env/bin/activate`
	1. Your command prompt should read something similar to `(my_project_env)user@host:~/sageWorkspace$`
	2. **Note:** Always activate your virtual environment whenever you start working with the packages you install within it and for Sage related tasks. And deactivate it with `(my_project_env)user@host:~$ deactivate` when you are done working.
	3. With this virtual environment, site packages and dependencies can be organized separate from the rest of the machine, so always be conscious of where you are working
8. We will now add an important command to the startup files of the terminal, so that packages install and run correctly in the virtual environment
	1. Deactivate your virtual environment and run the command `$ vi ~/.bashrc` 
	2. Click the letter "i" on your keyboard to go into insert mode (able to edit the file)
	3. Use your arrow keys to go to the bottom of the file
	4. Add the command `export OPENBLAS_CORETYPE=ARMV8` at the very bottom, and you can choose to add a comment on top of it saying "Resolves illegal construction error and package installation errors"
	5. Click the "escape" key on your keyboard, type ":wq", and hit "enter" or "return" on your keyboard
9. You now have a working virtual environment!
	1. **Important:** Never install packages using `(my_project_env)user@host:~$ sudo ...` commands within the virtual environment because it will cause dependency issues, so instead, install packages with `(my_project_env)user@host:~$ pip install ...`