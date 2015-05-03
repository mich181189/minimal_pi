

busybox = {
             "name": "busybox",
             "source":"http://busybox.net/downloads/busybox-1.23.2.tar.bz2",
             "buildDir":"busybox-1.23.2",
             "dependencies":["libtirpc"],
             "extraScripts": ["fixBusyboxConfig.py"],
             "extraFiles": {"busybox.config":".config"},
             "configure": "", #busybox doesn't use configure
             "extraInstall": {"examples/inittab":"/etc/inittab",
             					"examples/inetd.conf":"/etc/inetd.conf",
             					"examples/mdev.conf":"/etc/mdev.conf"}
          }