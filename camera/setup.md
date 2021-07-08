<h1>Camera Setup</h1>

1. Plug in the camera's power adapter into an outlet and plug in the camera.
2. Plug one end of the ethernet cord into the camera and the other into the Nano.
3. Install `tshark` on the Nano by running the following command:  
  `sudo apt install tshark`  
    1. `tshark` is an application that will allow us to look at the data packets being sent by the camera.
    
4. Run `tshark` by simply running the following command:
  `tshark`
    1. If it returns a message saying permission was denied, run it using `sudo`:  
      `sudo tshark`
    2. It should say `Capturing on 'eth0'`
    
5. Look for a line that contains the word "Amcrest," similar to this:  
  `1 0.000000000 AmcrestT_2f:d6:78 → Broadcast    ARP 60 Who has 192.168.1.1? Tell 192.168.1.108`  
    1. The important part of this is the very last number, after the word "Tell".  
    This is the IP adress of the camera. Make note of this, as you will need this to stream video from it.
    
<h2>Now the camera is all set up!</h2>

See `camera/videoStream.ipynb` to learn how to stream video from the camera using Python.
