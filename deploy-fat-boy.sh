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
apt-get install docker-compose -y
print 'Docker install'

#C2 install
git clone https://github.com/its-a-feature/Mythic
print 'C2 install'

#C2 docker build
cd Mythic
#Password changes
./mythic-cli config set MYTHIC_ADMIN_PASSWORD Tijolo22!
./mythic-cli config set POSTGRES_PASSWORD Tijolo22!
./mythic-cli config set RABBITMQ_PASSWORD Tijolo22!
#Opening to web
./mythic-cli config set RABBITMQ_BIND_LOCALHOST_ONLY false
./mythic-cli config set MYTHIC_SERVER_BIND_LOCALHOST_ONLY false
#Changing server
./mythic-cli config set NGINX_PORT 443
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

#Exposing to web
./mythic-cli config c2 -y
