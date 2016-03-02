#
#  NetworkDrill by Raspberry
#

#Start Up
clear

#Install Upadtes
if [ "$1" != "--no-update" ]
then
	sudo apt-get update
	sudo apt-get upgrade -y
fi

# Install Ettercap
sudo apt-get install zlib1g zlib1g-dev -y
sudo apt-get install build-essential -y
sudo apt-get install ettercap -y
sudo apt-get update
sudo apt-get install ettercap-text-only -y

