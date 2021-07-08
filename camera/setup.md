<h1>Camera Setup</h1>

1. Connect the power adapter to the camera

2. Connect one end of the ethernet cord to the camera and the other to the Nano's ethernet port

3. On the Nano, install the `tshark` application by running the following command:
  `sudo apt install tshark`
  
4. Run `tshark` by running the following command:
  `sudo tshark`
    1. It should start scanning on `eth0`
    
5. When you see a line containing something about an Amcrest device stop `tshark` by pressing `control` + `c`

6. The line should say something along the lines of "`... Tell [IP Adress]`"
    1. Note the IP Adress that follows the word "Tell," this is your camera's IP Adress

<h2>The camera is all set up now and ready for you to use!</h2>

See `camera/videoStream.ipynb` for more information on the camera including how to interact with it using Python.
