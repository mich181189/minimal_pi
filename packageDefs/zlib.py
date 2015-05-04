#http://zlib.net/zlib-1.2.8.tar.gz
import os
zlib = {
             "name": "zlib",
             "source":"http://zlib.net/zlib-1.2.8.tar.gz",
             "buildDir":"zlib-1.2.8",
             "dependencies":[],
             "envVars": {
                "CC":os.environ["MINIMALPI_ARCH"]+"-gcc",
                "CFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target",
                "LDFLAGS":"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target"
                },
             "configure":"./configure --prefix=/usr"
          }