<h1>Camera Setup</h1>

1. Plug in the camera's power adapter into an outlet and plug in the camera.
2. Plug one end of the ethernet cord into the camera and the other into the Nano.
3. On the Nano, open the system settings
4. Go to Network
5. Click on each of the connections labeld "Wired" and look for the one that says "Connected - 100Mb/s"
    1. This is the camera
6. Click on options
7. Go to the IPv4 settings tab
8. Click on the "Method" dropdown and select "Shar to other computers"
9. Check the box next to "Require IPv4 addressing for this connection to complete
10. Click save
11. Install `tshark` on the Nano by running the following command:  
  `sudo apt install tshark`  
    1. `tshark` is an application that will allow us to look at the data packets being sent by the camera.   
12. Run `tshark` by simply running the following command:
  `tshark`
    1. If it returns a message saying permission was denied, run it using `sudo`:  
      `sudo tshark`
    2. It should say `Capturing on 'eth0'`   
13. Look for a line that contains the word "Amcrest," similar to this:  
  `1 0.000000000 AmcrestT_2f:d6:78 → Broadcast    ARP 60 Gratuitous ARP for 10.42.0.54`  
    1. The important part of this is the very last number, after the words "ARP for".  
    This is the IP adress of the camera. Make note of this, as you will need this to stream video from it.
    
<h2>Now the camera is all set up!</h2>

See `camera/videoStream.ipynb` to learn how to stream video from the camera using Python.
