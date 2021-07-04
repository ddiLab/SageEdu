<h1> Headless Mode Setup</h1>

This directory contains instructions on how to set up your Jetson Nano in headless mode.  
Headless mode does not require a monitor, mouse, or keyboard to be connected to the nano. All you need is another computer!

<h2>Useful Stuff</h2>

<h3>Connecting to Nano</h3> 

 * `ssh [USERNAME]@[NANO NAME].local`

<h3>Screen Commands</h3>

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

<h3>Jupyter Notebook</h3>

 * Start Without Browser:  
   * `jupyter notebook --no-browser --port 8080`
 * Setup SSH Tunnel:  
   * `ssh -NL 8080:localhost:8080 [USERNAME]@[NANO NAME].local`

<h2>Directory Contents</h2>

<h2>setup.md</h2>

  * This contains instructions on how to perform the basic initial setup of the Nano

<h2>jupyter.md</h2>

  * This contains instructions on how to install and run jupyter notebooks on the Nano

<h2>screen.md</h2>

  * This contains instructions on how to install and use the Screen application on the Nano

<h2>/images</h2>
  
  * A directory containing images referenced in the instructions

<h2>readme.md</h2>

  * This file
