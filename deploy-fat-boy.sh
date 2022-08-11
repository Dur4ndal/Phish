#!/usr/bin/bash

TEXT_RESET='\e[0m'
TEXT_YELLOW='\e[0;33m'
TEXT_RED_B='\e[1;31m'

#Print function
function print () {
	echo -e $TEXT_YELLOW
	echo $1' finished, proceeding...'
	echo -e $TEXT_RESET
}

#First build
echo -e $TEXT_RED_B
echo 'Would you like to install and update all requirements ? Y/n'
echo -e $TEXT_RESET
read -n 1 answer
if [ $answer == "y" ] || [ $answer == "n" ]; then
	if [ $answer == "y" ]; then

		#Update && Upgrade && Autoremove
		apt update -y
		print 'APT update'

		apt upgrade -y
		print 'APT upgrade'

		apt autoremove -y
		print 'APT autoremove'

		#git install
		apt install git -y
		print 'Git install'

		#docker.io install
		apt-get install docker.io -y
		print 'Docker install'
	fi

	#C2 install
	git clone https://github.com/its-a-feature/Mythic
	print 'C2 install'

	#C2 docker build
	cd Mythic
	./mythic-cli start
	print 'C2 up'

	./mythic-cli install github https://github.com/MythicAgents/Apollo
	./mythic-cli install github https://github.com/MythicAgents/apfell
	./mythic-cli install github https://github.com/MythicAgents/poseidon
	./mythic-cli install github https://github.com/MythicC2Profiles/http
	./mythic-cli install github https://github.com/MythicC2Profiles/dynamichttp
	echo -e $TEXT_YELLOW
	echo 'Payloads and Profiles loaded. Ready to go !'
	echo -e $TEXT_RESET
	cat .env | grep -i user
	cat .env | grep -i password
	cat .env | grep -i secret
fi

