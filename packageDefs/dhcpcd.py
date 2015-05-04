
import os

dhcpcd = {
             "name": "dhcpcd",
             "source":"http://roy.marples.name/downloads/dhcpcd/dhcpcd-6.8.2.tar.bz2",
             "buildDir":"dhcpcd-6.8.2",
             "dependencies":[],
             "extraconfig":"--without-udev --sysconfdir=/etc",
          }