#! /usr/bin/python

import os, struct, time
from fcntl import ioctl

# Linux specific...
# TUNSETIFF ifr flags from <linux/tun_if.h>

IFF_TUN		= 0x0001   # tunnel IP packets
IFF_TAP		= 0x0002   # tunnel ethernet frames
IFF_NO_PI	= 0x1000   # don't pass extra packet info
IFF_ONE_QUEUE	= 0x2000   # ???

def main():
    mode = IFF_TAP | IFF_NO_PI
    TUNSETIFF = 0x400454ca

    tun = os.open("/dev/net/tun", os.O_RDWR)
    ifs = ioctl(tun, TUNSETIFF, struct.pack("16sH", "lvl%d", mode))
    ifname = ifs[:16].strip("\x00")
    print ifname
    #os.system("sudo ifconfig 192.168.200.1 lvl0")
    print "virtual interface created"
    while True:
    	#os.write(tun, "TEST")
        time.sleep(1)

if __name__ == '__main__':
    main()