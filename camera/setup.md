<h1>Camera Setup</h1>

1. Plug in the camera's power adapter into an outlet and plug in the camera.
2. Plug one end of the ethernet cord into the camera and the other into the Nano.

<h2>Headful</h2>

1. On the Nano, open the system settings
2. Go to Network
3. Click on each of the connections labeld "Wired" and look for the one that says "Connected(ing) - 100Mb/s"
    1. This is the camera
4. Click on options
5. Go to the IPv4 settings tab
6. Click on the "Method" dropdown and select "Shared to other computers"
7. Check the box next to "Require IPv4 addressing for this connection to complete
8. Click save

<h2>Headless Mode only</h2>

1. Install nmcli on the Nano by running the following command:  
        `sudo apt install network-manager`  
2. Check your active connections by running the following command:  
        `nmcli connection show`  
        1. One of the connections should have the type `ethernet` and the device as `eth0`, this is the camera  
        2. Make note of the name of this connection  
3. Set up IPv4 sharing for the camer by running the following command:  
        `nmcli connection modify CONNECTION_NAME ipv4.method shared`  
        1. Where `CONNECTION_NAME` is replaced by the name of the connection you noted in the previous step

<h2>Finding the Camera's IP Adress</h2>

1. Install `tshark` on the Nano by running the following command:  
  `sudo apt install tshark`
    1. If using a virtual environment, deactivate it first and then run the above command 
    2. `tshark` is an application that will allow us to look at the data packets being sent by the camera.   
2. Run `tshark` by simply running the following command:
  `tshark`
    1. If it returns a message saying permission was denied, run it using `sudo`:  
      `sudo tshark`
    2. Again, run the above command on root system, not in virtual environment 
    2. It should say `Capturing on 'eth0'`   
3. Look for a line that contains the word "Amcrest," similar to this:  
  `1 0.000000000 AmcrestT_2f:d6:78 → Broadcast    ARP 60 Gratuitous ARP for 10.42.0.54`  
    1. The important part of this is the very last number, after the words "ARP for".  
    This is the IP adress of the camera. Make note of this, as you will need this to stream video from it.
    
<h2>Now the camera is all set up!</h2>

See `Stream.ipynb` and `WaggleStream.ipynb` to learn how to stream video from the camera using Python.
