# Setting up Jupyter Notebook
Make sure you have the jupyter package installed on your virtual enviornment by running the command:  
    `pip list`  
If you don't see the jupyter package listed, see the [Package Installation Guide](https://github.com/ddiLab/SageEdu/blob/main/setup/general/PackageInstallationGuide.md) on how to install it.

---

## Headful Mode
1. Start a jupyter notebook server by running the command  
    `jupyter notebook`
2. This will start up a browser and display a Jupyter Notebook
3. Refer to the instructions at the bottom if you receive errors in the terminal

## Headless Mode
1. Start a Jupyter Notebook by running the following command:  
    `jupyter notebook --no-browser --port 8080`  
    * The `--no-browser` flag tells jupyter no to open up a browser   
    * The `--port 8080` flag tells jupyter to run the server on port 8080  
    * Make note of the URL it gives you that looks something like this:  
       ` http://localhost:8888/?token=8d1860e09abd435665a546fcc15b68683c99`  
2. On your computer, in a different terminal session than the one running the Jupiter notebook, run the following command:  
    `ssh -NL 8080:localhost:8080 [USERNAME]@[NANO NAME].local`  
    * This sets up ssh tunnling which allows your computer to connect to the specified port on the Nano and access the Jupyter notebook
3. In a browser on your computer paste the URL that you got from the first step

---

**Next from your Jupyter notebook session, open the `/setup/general/jupyterNotebookTutorial.ipynb` notebook for a brief tutorial on using Jupyter notebooks!**

---

### How to deal with the error "Error: Can't initialize nvrm channel" in Headful Mode:
1. Exit all browsers and type "Ctrl + C" in the terminal to exit out of the notebook
2. Once Jupyter Notebook is no longer running, open a browser window, make that browser the default browser, and rerun the command from step 1
3. Note: It's possible that a window from the default browser must always be open before starting Jupyter Notebook
