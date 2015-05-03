#http://www.nano-editor.org/dist/v2.4/nano-2.4.1.tar.gz


import os

nano = {
             "name": "nano",
             "source":"http://www.nano-editor.org/dist/v2.4/nano-2.4.1.tar.gz",
             "buildDir":"nano-2.4.1",
             "dependencies":["ncurses"],
             "patches":["nano.patch"],
             "envVars": {
             	"CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target",
             	"LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target"
             	},
             	"extraconfig":"--enable-utf8=no"
          }