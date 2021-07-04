
<h1>Using Screen on the Headless Nano</h1>

Screen is an very useful terminal application. It essentially lets you save your progess in an SSH sesion. 
If you are working on a terminal session while using Screen, and for some reason you are disconnected from the Nano, Screen will save what you were doing.
This means that when you go back to the terminal, it will take you back to the same screen you were on before.
You can also use screen in order to leave scripts or other things running on the Nano, without having to be connected to it the entire time.

Before you continue you must first be in your Nano's terminal which can be done via the following command:  
  `ssh [USERNAME]@[NANO NAME].local`
  
1. Install Screen on the Nano by running the following command:
  `sudo apt install screen`  
  
2. Run the following command:  
  `screen -ls`
    1. The `-ls` flag tells screen to print a list of all the screen sessions that are running. Make note of this command as it will be very useful in the future.
    2. It should return a message that looks something like this:  
    `No Sockets found in /run/screen/S-username.`
    3. This means there are no screen sessions currently running
  
3. Start a screen session by simply running:  
  `screen -S [NAME]`
    1. Where `[NAME]` is replaced by a name you give to the screen session  
    2. You should see a screen that looks like this:  
    <img alt='screen prompt' src=''></img>
    3. Follow the prompts on screen
  
4. Now print a list of all the screen sessions that are running using the command from step 2.
    1.  You should now see something like this:  
    `There is a screen on:`  
    `    8350.name (07/04/2021 10:22:51 AM)        (Attached)`  
    `1 Socket in /run/screen/S-username.`

    2. The information we care about is in the second line.  
     The first part before the date and time in parentheses is the name of the screen session.  
     After the date and time comes the status of the session. Attached means it is in use. Detached means it's running but not in use.

5. Detach the current screen session by running the following command:  
  `screen -d [SESSION NAME]`
    1. Where `[SESSION NAME]` is replaces by the name of your screen session that you found in step 4.
    2. The `-d` flag detaches the given session.

6. Now print a list of all the screen sessions that are running as you did in step 4.
    1. The output should be the same as it was in step 4 except that now it should say the session is Detached.

7. Reattach to the session by running the following command:  
  `screen -r [SESSION NAME]`
  1. The `-r` flag reattaches the given session.

8. Exit and quit the current session that is attached simply by running the following command:  
  `exit`
