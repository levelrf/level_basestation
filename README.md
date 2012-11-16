steps for prepping base station server:
(should eventually have all of this in a distro that we can install on new basestations)

install ubuntu:
username = level
password = levelrf!!!

  log in to router, set up server local IP to be static
  forward port 80 to that IP

crontab -e
then add this job:
00 * * * * /home/level/updateip.sh

make sure updateip.sh is in the correct folder
touch ip.txt and add 0.0.0.0

so this will check the current external IP every hour and if it's changed, it will email my levelrf account and with the subject being the hostname and the message body being the new ip

installing gnuradio prereqs:
sudo apt-get -y install git-core autoconf automake  libtool g++ python-dev swig \
pkg-config libboost-all-dev libfftw3-dev libcppunit-dev libgsl0-dev \
libusb-dev sdcc libsdl1.2-dev python-wxgtk2.8 python-numpy \
python-cheetah python-lxml doxygen python-qt4 python-qwt5-qt4 libxi-dev \
libqt4-opengl-dev libqwt5-qt4-dev libfontconfig1-dev libxrender-dev 

install uhd:
sudo apt-get install libboost-all-dev libusb-1.0-0-dev python-cheetah doxygen python-docutils
git clone git://code.ettus.com/ettus/uhd.git

installing additional level prereqs:
sudo apt-get -y install python-setuptools python-zmq
sudo easy_install crcmod

checkout our gnuradio fork:
git clone https://github.com/levelrf/level_basestation.git

config and build 
cd level_basestation
mkdir build
cd build
cmake ../
make

Installing MongoDB:
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10

Create a the /etc/apt/sources.list.d/10gen.list file and include the following line for the 10gen repository.

deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen

sudo apt-get update

sudo apt-get install mongodb-10gen

sudo /etc/init.d/mongodb start

pip install pymongo


