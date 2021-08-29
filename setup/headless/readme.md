# Headless Mode Setup

This directory contains instructions on how to set up your Jetson Nano in headless mode.  
Headless mode does not require a monitor, mouse, or keyboard to be connected to the nano. All you need is another computer!

---

## Useful Stuff

### Connecting to Nano
 * `ssh [USERNAME]@[NANO NAME].local`

### Screen Commands
 * New session:
   * `screen -S [NAME]`  
 * List Sessions:
   * `screen -ls`  
 * Detatch Session:
   * `screen -d [NAME]`  
 * Reattach Session:
   * `screen -r [NAME]`
 * Exit and Quit:
   * `exit`

### Jupyter Notebook
 * Start Without Browser:  
   * `jupyter notebook --no-browser --port 8080`
 * Setup SSH Tunnel:  
   * `ssh -NL 8080:localhost:8080 [USERNAME]@[NANO NAME].local`

---

## Directory Contents

### [setup.md](https://github.com/ddiLab/SageEdu/blob/main/setup/headless/setup.md)
  * This contains instructions on how to perform the basic initial setup of the Nano

### [jupyter.md](https://github.com/ddiLab/SageEdu/blob/main/setup/headless/jupyter.md)
  * This contains instructions on how to install and run jupyter notebooks on the Nano

### [screen.md]()
  * This contains instructions on how to install and use the Screen application on the Nano

### [images/](https://github.com/ddiLab/SageEdu/tree/main/setup/headless/images)
  * A directory containing images referenced in the instructions

### [readme.md](https://github.com/ddiLab/SageEdu/blob/main/setup/headless/images/readme.md)
  * This file
