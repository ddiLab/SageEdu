## Creating a virtual environment to use as a workspace for project related tasks
1. Within the terminal, install python 3 and related packages using the command `$ sudo apt install python3-pip python3-dev`
2. Make sure to have every package on your system up-to-date by running the commands `$ sudo apt update` and `$ sudo apt upgrade`, so there aren't any dependency issues
3. Then run `$ python3 -m pip install --upgrade pip` to upgrade pip
4. Run the command `$ sudo -H pip3 install virtualenv` to install the ability to construct a virtual environment
5. Create a directory on your computer related to all project tasks (e.g., `/Workspace`). This directory will store your virtual environment and Github repo (if you are using one)
6. Use the command `$ virtualenv /my_project_env` within `/Workspace`, where `/my_project_env` is the name of the virtual environment you want to create, so make sure to name it appropriately 
	1. **Important:** Do not ever edit this folder
7. Activate the environment with the command `$ source my_project_env/bin/activate`
	1. Your command prompt should read something similar to `(my_project_env)user@host:~/Workspace$`
	2. **Note:** Always activate your virtual environment whenever you start working with the packages you install within it and for Sage related tasks. And deactivate it with `(my_project_env)user@host:~$ deactivate` when you are done working.
	3. With this virtual environment, site packages and dependencies can be organized separate from the rest of the machine, so always be conscious of where you are working
8. Run the command `(my_project_env)user@host:~$ python3 -m pip install --upgrade pip`
9. We will now add an important command to the startup files of the terminal, so that packages install and run correctly in the virtual environment
	1. Deactivate your virtual environment and run the command `$ vi ~/.bashrc` 
	2. Click the letter "i" on your keyboard to go into insert mode (able to edit the file)
	3. Use your arrow keys to go to the bottom of the file
	4. Add the command `export OPENBLAS_CORETYPE=ARMV8` at the very bottom, and you can choose to add a comment on top of it saying "# resolves illegal construction error and package installation errors"
	5. Click the "escape" key on your keyboard, type ":wq", and hit "enter" or "return" on your keyboard
	6. Exit out of all terminal windows because the change only takes place in new terminal windows 
10. You now have a working virtual environment!
	1. **Important:** Never install packages using `(my_project_env)user@host:~$ sudo ...` commands within the virtual environment because it will cause dependency issues, so instead, install packages with `(my_project_env)user@host:~$ pip install ...` or any other way that does not run root permissions within the virtual environment (e.g., `(my_project_env)user@host:~$ python3 -m pip install ...`). But if it's necessary to install something to root, do so outside of the virtual environment (e.g., installing tshark, libportaudio2). Though, this may require you to run the program outside of the virtual environment. If in doubt, look up what each part of a command does 
11. Everything that can be done by a system setup can be done within a virtual environment. Just make sure to intall the appropriate packages correctly
