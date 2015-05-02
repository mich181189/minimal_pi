import sys

def patchBusyboxConfig(package):
    pass

busybox = {
             "name": "busybox",
             "source":"http://busybox.net/downloads/busybox-1.23.2.tar.bz2",
             "buildDir":"busybox-1.23.2",
             "dependencies":[],
             "extraScripts": ["fixBusyboxConfig.py"],
             "extraFiles": {"busybox.config":".config"},
             "configure": "" #busybox doesn't use configure
          }