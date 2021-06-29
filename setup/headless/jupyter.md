<h1>How to Use Jupyter Notebooks in Headless Mode</h1>

You must be coneected to your Nano via ssh:  
  `ssh [USERNAME]@[NANO NAME].local`
  
1) Start a Jupyter Notebook by running the following command:  
  `jupyter notebook --no-browser --port 8080`
    1) The `--no-browser` flag tells jupyter no to open up a browser   
        - We want this because we don't have a monitor
    2) The `--port 8080` flag tells jupyter to run the server on port 8080
    3) Make note of the URL it gives you that looks something like this:  
      `http://localhost:8888/?token=8d1860e09abd435665a546fcc15b68683c99`
      
2) On your computer in a different terminal session than the one running the Jupiter notebook, run the following command:  
  `ssh -NL 8080:localhost:8080 [USERNAME]@[NANO NAME].local`
    1) This sets up ssh tunnling which allows your computer to connect to the specified port on the Nano and access the Jupyter notebook
  
3) In a browser on your computer paste the URL that you got from the first step

<h3>Now you can use Jupyter notebooks on the Nano!</h3>
