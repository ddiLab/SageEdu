## Setting up Jupyter Notebook
1. If using a virtual environment, make sure to activate it first and run the command `(my_project_env)user@host:~$ pip install jupyter`
2. If not using a virtual environment, run the command `$ python3 -m pip install jupyter`
3. To create a notebook, run the command `jupyter notebook`. It doesn't matter if it's in a virtual environment or not.  
4. This will start up a browser and display a Jupyter Notebook
5. How to deal with the error "Error: Can't initialize nvrm channel" :
	1. Exit all browsers and type "Ctrl + C" in the terminal to exit out of the notebook
	2. Once Jupyter Notebook is no longer running, open a browser window, make that browser the default browser, and rerun the command from step 3 
	3. Note: It might be that a window from the default browser must always be open before opening Jupyter Notebook
6. To exit out of Jupyter Notebook, type "Ctrl + C" in the terminal where the notebook is running
