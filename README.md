
# NetCrow - by Raspberryy

This is a fun little Tool made for the Raspberry Pi!

But of course it can be used on every Linux System... <br />
It is using python Code to execute the MiTM automatically. <br />
The Attack itself is using ettercap to analyize Network Traffic. <br />

The main Features are:
 - Automatic start at Boot (if needed)
 - Sending gathered Data via E-Mail to the User
 - Autosaving 

# Installing NetCrow
  sudo -i <br />
  cd to/path/you/want/to/install <br />
  git clone https://github.com/Raspberryy/NetCrow.git <br />
  sh install.sh

# Installing Automatic Boot
  sudo python AutoStart.py

# Configure E-Mail Sending
  nano attack.py
    
    Enter your E-Mail Data:
    Sender = "YourGmailAdress@gmail.com"
    Password = "YourGMailPassword"
    Reciever = "YourEMailAdress@anyhost.com"

 
